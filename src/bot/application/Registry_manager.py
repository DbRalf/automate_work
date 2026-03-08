#application.registry_manager
from abc import ABC, abstractmethod


class RegistryManager(ABC):
    @abstractmethod
    def get_company_name(self, email: dict) ->str:
        pass

    @abstractmethod
    def get_worker_name(self, email: dict) ->str:
        pass