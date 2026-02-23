class CompanyNameNotFound (Exception):
    """Raised for undefinde company name """
    pass

class KeywordNotFound (Exception):
    """Raised if keyword not in list"""
    pass

class NotExpectedHours (Exception):
    """extraction is not the hours we wanted"""
    pass

class FailedMailExtraction (Exception):
    """Mail is recived and nothing got out of there"""
    pass