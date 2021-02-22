class ClientNotFound(Exception):
    """ CPF of client not found """
    pass


class Unauthorized(Exception):
    """ CPF and Cellphone of client don't match """
    pass
