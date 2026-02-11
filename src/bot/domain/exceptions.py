class InvalidHours(Exception):
    """ Raised when hours are negative """
    pass

class NotValidMonth(Exception):
    """ Raised for months not from 12 - 1"""
    pass

class ValidMailAddress(Exception):
    """ Raised when @ and .com not in the mail """
    pass