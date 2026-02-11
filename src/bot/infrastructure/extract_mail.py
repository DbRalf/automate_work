from src.bot.domain import EmployeeRegistry


def get_mail_info():
    # claude will fill it in
    #
    # will return a variable containing the header body and all the information of the mail,
    # from what I read you get a dictionary with a json-like format, so you pass it to me
    # additionally you return the files, there can be multiple files!
    pass

class IsWorker(EmployeeRegistry):
    def in_registry(self, email: str) -> bool:
        """
        :param email:

        :return bool:
        """
        return True

def in_workers_list(mail_address) -> bool:
    """
    :param mail_address:

    check the json file if the mail exsists
    if yes - we continue return company name
    if not - we log it

    :return in_list:
    """
    pass

 ## what will the json have - email: name, company name

def extract_message(json_like_variable):
    # here I handle the extracting of the json like variable, it will search for a format or key-words


    # check if the body is empty- if yes then return hours=None
    # if no hours are found log it - if not found return hours=None and log
    pass

def extract_file(files, company_name):
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
    pass

def hour_extractor():
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

    pass