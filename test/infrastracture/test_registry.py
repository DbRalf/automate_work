import pytest

from src.bot.infrastructure.registry_adaptor import RegistryAdaptor
# class RegistryTest:
#     def __init__(self):
#         self.registry = RegistryAdaptor()

def test_registry_pull():
    registry = RegistryAdaptor()
    test_mail = "autorash03@gmail.com"
    company_name = registry.get_company_name(email=test_mail)
    print(f"========={company_name}========_____")