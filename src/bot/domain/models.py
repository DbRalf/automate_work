from abc import ABC, abstractmethod

from exceptions import *


class Worker:
    def __init__(self, name: str, mail: str):
        self._valid_mail(mail)
        self.name = name
        self.mail =mail

    @staticmethod
    def _valid_mail(mail: str) -> None:
        if not "@" in mail and not ".com" in mail:
            raise ValidMailAddress ("mail must contain @ and .com")


class HoursReport(Worker):
    def __init__(self, name: str, mail: str, month: int, work_days: int, hours: float):
        super().__init__(self, name, mail)
        # self.mail_id = ""
        self._valid_hours(hours, work_days)
        self._valid_month(month)
        self.month = month
        self.hours = hours

    @staticmethod
    def _valid_month(month: int) -> None:
        if 1 <= month <= 12:
            raise NotValidMonth ("month needs to be from 12 - 1")


    @staticmethod
    def _valid_hours(hours: float, work_days: int) -> None:
        full_hours = work_days * 8.4 # working day is 8.4 hours
        if hours < 0:
            raise InvalidHours ("Hours can't be negative")
        if 0 < hours < full_hours / 2:
            raise LowRelativeHours ("Low amount of hours for the month, half of the max")
        if hours > full_hours:
            raise OverTimeHours ("Overtime hours reached")



class EmployeeRegistry:
    @abstractmethod  # cannot create this class + makes sure all function are implemented
    def in_registry(self, email: str) -> bool:
        pass


