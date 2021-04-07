class UnableToAuthException(Exception):
    
  def __init__(self, payload=None):
    Exception.__init__(self)
    self.message = 'Não foi possível autorizar o cliente'

    self.status_code = 403
    self.payload = payload
    
  def to_dict(self):
    rv = dict(self.payload or ())
    rv['status_code'] = self.status_code
    rv['message'] = self.message
    return rv