import time
from asyncore import write

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
        :param mail_address:

        check the json file if the mail exsists
        if yes - we continue return company name
        if not - we log it

        :return bool:
        """
        return True

 ## what will the json have - email: name, company name


def main():
    pass


if __name__ == "__main__":
    main()