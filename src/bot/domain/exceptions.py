class InvalidHours(Exception):
    """ Raised when hours are negative """
    pass

class OverTimeHours(Exception):
    """ Raised when given hours exceed normal monthly hours cap"""
    pass

class LowRelativeHours(Exception):
    """ Raised when low amount of hours relative to monthly cap"""
    pass

class NotValidMonth(Exception):
    """ Raised for months not from 12 - 1"""
    pass

class ValidMailAddress(Exception):
    """ Raised when @ and .com not in the mail """
    pass