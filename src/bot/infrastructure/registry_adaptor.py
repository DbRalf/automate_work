# infrastructure.registry_adaptor
import yaml
import os
import sys

from src.bot.application.Registry_manager import RegistryManager
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))
REGISTRY_PATH = os.path.join(PROJECT_ROOT, "config", "data","workers_registry.yml")


class RegistryAdaptor(RegistryManager):
    def __init__(self):
        with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
            self.dict = yaml.safe_load(f)

    def get_company_name(self, email: str) ->str:
        email_list = self.dict["worker_dictionary"]
        worker = email_list.get(str(email))
        return worker["company_name"]

    def get_worker_name(self,email: str) -> str:
        email_list = self.dict["worker_dictionary"]
        worker = email_list.get(str(email))
        return worker["worker_name"]


    # future functions : add and remove worker
    #                   change_company_name ...?
