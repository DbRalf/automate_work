class InvalidHours(Exception):
    """ Raised when hours are negative """
    pass

class NotValidMonth(Exception):
    """ Raised for months not from 12 - 1"""
    pass

class InvalidMailAddress(Exception):
    """ Raised when @ and .com not in the mail """
    pass


class NotInRegistry(Exception):
    """Worker is nor found in the list of valid workers"""
    pass