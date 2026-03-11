import pytest
import re
from src.bot.application.exceptions import FailedMailExtraction
import src.bot.infrastructure.gmail_adaptor
from src.bot.infrastructure.gmail_adaptor import GmailAdaptor


def test_mail_reciving ():
    rec_mail = GmailAdaptor()
    mail_list = rec_mail.get_mail_info()
    for plain_text, files in mail_list:
        if not plain_text or not files:
            raise FailedMailExtraction

        print(plain_text)
        print(f"date is: {plain_text['Date']}")
        print(f"header is: {plain_text['Subject']}")
        print(plain_text['body'])
        print(plain_text["From"])
        # print(files[0].read())


