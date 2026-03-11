#application.pipelines

"""
this file contains all the functions that handle a complete event
email reciving/sending, creating invoices or sending them and so on

"""
from idlelib.window import registry
from io import BytesIO
from exceptiongroup import catch

from src.bot.domain.models import HoursReport, EmployeeRegistry, Message
from src.bot.domain.exceptions import NotInRegistry
from src.bot.application.gmail_handler import GmailMassages
from src.bot.application.extractors import Extractor
from src.bot.application.Registry_manager import RegistryManager
from src.bot.application.sheets_handler import SheetsHandler

class MonthlyHours:
    def __init__(self, gmail:GmailMassages, pdf:Extractor, registry:RegistryManager, sheets: SheetsHandler):
        self.gmail_rec = gmail
        self.pdf_processor = pdf
        self.registry = registry
        self.sheets = sheets


    def process_mail(self):
        mail_list = self.gmail_rec.get_mail_info()

        # flatten the file list
        flat_list_files = []
        for _, files in mail_list:
            for file in files:
                flat_list_files.append(file)

        senders =[sender["From"] for sender, _ in  mail_list]

        company_names =[]
        for sender in senders:
            company = self.registry.get_company_name(sender)
            if not company:
                print('email is not in the registry!')
                # in the future will skip to the next mail
                continue
            company_names.append(company)

        hours = self.extract_files(files=flat_list_files, companies=company_names)

        # for mail_content, files in mail_list:
        #     sender =  mail_content["From"]
        #     company_name = self.registry.get_company_name(sender)
        #     if not company_name:
        #         print('email is not in the registry!')
        #         # in the future will skip to the next mail
        #         continue
        #     hours = self.extract_files(files= files,company= company_name)
        #     print(f"received hours from mail: {hours}")
        #
        #     worker_name = self.registry.get_worker_name(sender)
        #     self.sheets.write_hours(worker_name, hours)



    def extract_files(self, files, companies: list[str]) -> list[float]:

        hours = []
        list_of_pdf = self.pdf_processor.extract_pdf_table(files)
        list_of_content = [string_content.split() for string_content in list_of_pdf]

        for list_content, company in zip( list_of_content, companies):
            hours.append(
                self.pdf_processor.extract_by_name(table=list_content, company_name=company)
            )
            print(f"received hours from mail: {hours}")

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

