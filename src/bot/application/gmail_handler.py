# application.gmail_handler
# this file  is the connection to the API to the application layer

from abc import ABC, abstractmethod
from io import BytesIO

class GmailMassages(ABC):

    @abstractmethod
    def get_mail_info(self, query: str = "has:attachment filename:pdf is:unread") -> tuple[dict, list[BytesIO]]:
        """
        return the mail content, header, body, sender, files and so on
        """
        pass

