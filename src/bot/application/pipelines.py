#application.pipelines

"""
this file contains all the functions that handle a complete event
email reciving/sending, creating invoices or sending them and so on

"""

from io import BytesIO
from exceptiongroup import catch

from src.bot.domain.models import HoursReport, EmployeeRegistry, Message
from src.bot.domain.exceptions import NotInRegistry
from src.bot.application.gmail_handler import GmailMassages
from src.bot.application.extractors import Extractor
from src.bot.application.Registry_manager import RegistryManager

class MonthlyHours:
    def __init__(self, gmail:GmailMassages, pdf:Extractor, registry:RegistryManager):
        self.gmail_rec = gmail
        self.pdf_processor = pdf
        self.registry = registry


    def process_mail(self):
        mail_content, files = self.gmail_rec.get_mail_info()
        print(mail_content["From"])
        company_name = self.registry.get_company_name(mail_content["From"])
        if not company_name:
            print('email is not in the registry!')
            # in the future will skip to the next mail
            return
        hours = self.extract_files(files= files,company= company_name)
        print(f"received hours from mail: {hours}")


    def extract_files(self, files, company) -> float:
        hours = 0.0
        for file in files:
            string_content = self.pdf_processor.extract_pdf_table(file)
            list_content = string_content.split()
            hours = self.pdf_processor.extract_by_name(table=list_content, company_name=company)

        # cheack for valid hours from multiple files

        return hours








"""
json_var,files = get_mail_info()
from json_var get email
if not in_worker_list(email) -> wait for another mail / close program


mes_hours = extract_message(json_var)
file_hours = extract_file(files)

if mes_hours and file_hours are empty throw an exception
if mes_hours != file_hours print to the user the hours conflict

show the user the file of the hours
input("what hours are in the time sheets?/ confirm [C]") somthing across those lines

create HoursReport to check domain rules
if all is good
we save it to the db (IDK what is the db yet)

:return:
"""

