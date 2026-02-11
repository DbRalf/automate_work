import pytest


from src.bot.domain.exceptions import ValidMailAddress, InvalidHours
from src.bot.domain.models import Worker, HoursReport

def test_worker_reject_invalid_email():
    with pytest.raises(ValidMailAddress):
        Worker(name="Nugget", mail="invalid-mail")

def test_hours_report_rejects_overtime():
    with pytest.raises(InvalidHours):
        HoursReport(name="Nigget", mail="M@test.com", month=1, hours=-999, work_days=21)