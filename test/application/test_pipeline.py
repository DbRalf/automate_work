import pytest

from src.bot.application.pipelines import MonthlyHours
from src.bot.infrastructure.gmail_adaptor import GmailAdaptor
from src.bot.infrastructure.pdf_extractor import PDFMmanager
from src.bot.infrastructure.registry_adaptor import RegistryAdaptor
from src.bot.infrastructure.sheets_adaptor import SheetsAdaptor
def test_full_pipeline():
    p = PDFMmanager()
    g = GmailAdaptor()
    r = RegistryAdaptor()
    s = SheetsAdaptor()
    hours_mail = MonthlyHours(pdf=p, gmail=g, registry=r, sheets= s)
    hours_mail.process_mail()
    # hours_mail.hours_to_sheets