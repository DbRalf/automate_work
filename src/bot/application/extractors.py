# application/extractors

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
    def extract_by_name(table: list, company_name: str) -> int:
        hours = 0
        if company_name == "MOD":
            index = table.index('סה״כ:')
            hours = table[index - 3] # always 3 places away from סכ״ה
        elif company_name == "Harel":
            index = table.index('העובד:')
            hours = table[index - 3]
        elif company_name == "CP":
            index = table.index('Total(Decimal)')
            hours = table[index + 1]
        elif company_name == "Maccabi":
            index = table.index('הקיזוז')
            hours = table[index - 2]


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

