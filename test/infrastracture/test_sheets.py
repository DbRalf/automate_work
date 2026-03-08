import pytest

from src.bot.infrastructure.sheets_adaptor import SheetsAdaptor

def test_sheets_insert():
    sheets = SheetsAdaptor()
    sheets.write_hours(worker_name='דיויד ברמן',hours= 172.2)