class InvalidCPFException(Exception):

  def __init__(self, payload=None):
    Exception.__init__(self)
    self.message = 'O CPF informado é inválido'

    self.status_code = 400
    self.payload = payload
    
  def to_dict(self):
    rv = dict(self.payload or ())
    rv['status_code'] = self.status_code
    rv['message'] = self.message
    return rv