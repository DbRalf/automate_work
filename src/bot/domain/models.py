from abc import ABC, abstractmethod

from .exceptions import *

class Message:
    def __init__(self, email_address: str, email_body: str, email_header: str, files):
        self.address = email_address
        self.body = email_body
        self.header = email_header
        self.files = files

    def get_mail(self):
        return self.address



class Worker:
    def __init__(self, name: str, message: Message):
        self.name = name
        self.message = message

    @staticmethod
    def _valid_mail(mail: str) -> None:
        if not "@" in mail or not ".com" in mail:
            raise InvalidMailAddress ("mail must contain @ and .com")


class HoursReport:
    def __init__(self, worker:Worker, work_days=None,):
        self.work_days = work_days
        self.worker = worker
        self.hours = 0



    # def valid_month(self, month: int) -> None:
    #     if 1 > month > 12:
    #         raise NotValidMonth ("month needs to be from 12 - 1")
    #     self.month =month


    def hours_in_expected_range(self, hours) -> str:
        full_hours = self.work_days * 8.4
        if 0 < hours < full_hours / 2:
            return "under half of the max hours"
        if hours > full_hours:
            return "overtime hours"
        return ""


    def valid_hours(self, hours: float) -> None:
        if hours < 0 or self.hours_in_expected_range(hours):
            raise InvalidHours ("Hours can't be negative")

        self.hours = hours




class EmployeeRegistry:
#
#     @abstractmethod  # cannot create this class + makes sure all function are implemented
#     def _employ_in_registry(self, email: dict) -> str:
    pass
#



