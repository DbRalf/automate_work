import pytest

from src.bot.application.exceptions import FailedMailExtraction
import src.bot.infrastructure.gmail_adaptor
from src.bot.infrastructure.gmail_adaptor import get_mail_info


def test_mail_reciving ():
    plain_text, files = get_mail_info()
    if not plain_text or not files:
        raise FailedMailExtraction

    print(plain_text)
    print(files[0].read())


