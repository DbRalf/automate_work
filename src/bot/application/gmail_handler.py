# application.gmail_handler
# this file  is the connection to the API to the application layer

from abc import ABC, abstractmethod
from io import BytesIO

class GmailMassages(ABC):

    @abstractmethod
    def get_mail_info(self, query: str = "has:attachment filename:pdf is:unread") -> list[tuple[dict, list[BytesIO]]]:
        """
        return a list of (mail_content, files) tuples for all matching emails
        """
        pass

