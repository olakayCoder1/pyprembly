import prembly




class PremblyException(Exception):
    """The base exception class for all PremblyException"""
    pass


class MissingAuthKeyError(PremblyException):
    """
    We can't find the authentication/authorization key
    """
    pass