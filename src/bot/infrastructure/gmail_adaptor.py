import base64
import os
from io import BytesIO

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))
CREDENTIALS_PATH = os.path.join(PROJECT_ROOT, "config", "credentials.json")
TOKEN_PATH = os.path.join(PROJECT_ROOT, "config", "token.json")

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def _build_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)


def _extract_headers(headers: list) -> dict:
    wanted = {"From", "Subject", "Date"}
    return {h["name"]: h["value"] for h in headers if h["name"] in wanted}


def _extract_body(payload: dict) -> str:
    """Recursively walk the MIME tree and return the first plain-text body."""
    mime_type = payload.get("mimeType", "")

    if mime_type == "text/plain":
        data = payload.get("body", {}).get("data", "")
        return base64.urlsafe_b64decode(data + "==").decode("utf-8", errors="replace") if data else ""

    if mime_type.startswith("multipart/"):
        for part in payload.get("parts", []):
            text = _extract_body(part)
            if text:
                return text

    return ""


def _extract_attachments(service, user_id: str, message_id: str, payload: dict) -> list[BytesIO]:
    """Walk the MIME tree and download every PDF attachment as a BytesIO stream."""
    attachments = []

    def _walk(part):
        filename = part.get("filename", "")
        mime_type = part.get("mimeType", "")
        body = part.get("body", {})
        attachment_id = body.get("attachmentId")

        if attachment_id and (mime_type == "application/pdf" or filename.lower().endswith(".pdf")):
            response = (
                service.users()
                .messages()
                .attachments()
                .get(userId=user_id, messageId=message_id, id=attachment_id)
                .execute()
            )
            data = base64.urlsafe_b64decode(response["data"] + "==")
            stream = BytesIO(data)
            stream.name = filename
            attachments.append(stream)

        for sub_part in part.get("parts", []):
            _walk(sub_part)

    _walk(payload)
    return attachments


def get_mail_info(query: str = "has:attachment filename:pdf is:unread") -> tuple[dict, list[BytesIO]]:
    """
    Fetch the most recent email matching *query* from Gmail.

    Returns:
        mail_info  – dict with keys: From, Subject, Date, body
        attachments – list of BytesIO streams (one per PDF attachment)

    Raises:
        HttpError if the Gmail API call fails.
        ValueError if no matching email is found.
    """
    service = _build_service()

    results = service.users().messages().list(userId="me", q=query, maxResults=1).execute()
    messages = results.get("messages", [])
    if not messages:
        raise ValueError(f"No emails found matching query: '{query}'")

    message_id = messages[0]["id"]
    message = service.users().messages().get(userId="me", id=message_id, format="full").execute()

    payload = message["payload"]
    headers = _extract_headers(payload.get("headers", []))
    headers["body"] = _extract_body(payload)

    attachments = _extract_attachments(service, "me", message_id, payload)

    return headers, attachments
