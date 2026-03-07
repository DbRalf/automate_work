# infrastructure.sheets_adaptor
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from src.bot.application.sheets_handler import SheetsHandler


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))
CREDENTIALS_PATH = os.path.join(PROJECT_ROOT, "config", "credentials.json")
SHEETS_TOKEN_PATH = os.path.join(PROJECT_ROOT, "config", "sheets_token.json")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1x9-TFDZ1atjIt4d1s9itGqCyi00t28bfLSN9OmQH5FY"
SHEET_NAME = "Sheet1"


class SheetsAdaptor(SheetsHandler):

    def _build_service(self):
        creds = None
        if os.path.exists(SHEETS_TOKEN_PATH):
            creds = Credentials.from_authorized_user_file(SHEETS_TOKEN_PATH, SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(SHEETS_TOKEN_PATH, "w") as token:
                token.write(creds.to_json())
        return build("sheets", "v4", credentials=creds)

    def write_hours(self, worker_name: str, hours: float) -> None:
        service = self._build_service()
        sheets = service.spreadsheets()

        result = sheets.values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!C:C"
        ).execute()

        names = result.get("values", [])

        row_index = None
        for i, row in enumerate(names):
            if row and row[0] == worker_name:
                row_index = i + 1  # Sheets API is 1-indexed
                break

        if row_index is None:
            raise ValueError(f"Worker '{worker_name}' not found in sheet")

        sheets.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!E{row_index}",
            valueInputOption="RAW",
            body={"values": [[hours]]}
        ).execute()
