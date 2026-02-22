# application/extractors
from src.bot.application.exceptions import  KeywordNotFound, CompanyNameNotFound, NotExpectedHours
from abc import  ABC, abstractmethod



class Extractor(ABC):

    def extract_message(self, json_like_variable):
        # here I handle the extracting of the json like variable, it will search for a format or key-words


        # check if the body is empty- if yes then return hours=None
        # if no hours are found log it - if not found return hours=None and log
        pass

    @abstractmethod
    def extract_pdf_table(self, file) -> str:
        pass

    @staticmethod
    def extract_by_name(table: list, company_name: str) -> float:
        hours = 0
        from_index = 0
        if company_name == "MOD":
            try:
                index = table.index('סה״כ:')
            except ValueError:
                raise KeywordNotFound
            from_index = -3

        elif company_name == "Harel":
            try:
                index = table.index('העובד:')
            except ValueError:
                raise KeywordNotFound
            from_index = -3

        elif company_name == "CP":
            try:
                index = table.index('Total(Decimal)')
            except ValueError:
                raise KeywordNotFound
            from_index = 1

        elif company_name == "Maccabi":
            try:
                index = table.index('הקיזוז')
            except ValueError:
                raise KeywordNotFound
            from_index = - 2

        else:
            raise CompanyNameNotFound

        hours = table[index + from_index]
        print(hours)
        try:
            hours = float(hours)
        except ValueError:
            raise NotExpectedHours

        if 0 > hours or hours > 250:
            raise NotExpectedHours

        return hours

"""
:param files: -> files that might contain the hours
:param company_name:
each company has its own way of writing hours sheets,
therefor each extraction is different but similar -> tables in a pdf

so extraction may include rotating the pdf to a known format,
cutting the only needed part and extracting from there

look into PyMUPDF, Tabula-py, camelot, pdfplumber
might not need complicated operations

:return: hours
"""



    # this part should go to infrastructure layer




def main():
    pass

if __name__ == "__main__":
    main()

