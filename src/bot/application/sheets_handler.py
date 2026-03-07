# application.sheets_handler
from abc import ABC, abstractmethod


class SheetsHandler(ABC):

    @abstractmethod
    def write_hours(self, worker_name: str, hours: float) -> None:
        """
        Find the worker by name in column C of the sheet and write their hours to column E.
        Raises ValueError if the worker name is not found.
        """
        pass
