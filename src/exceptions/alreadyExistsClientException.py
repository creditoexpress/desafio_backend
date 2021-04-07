class AlreadyExistsClientException(Exception):
  
  def __init__(self, payload=None):
    Exception.__init__(self)
    self.message = 'Este cliente já está cadastrado'
    
    self.status_code = 400
    self.payload = payload
    
  def to_dict(self):
    rv = dict(self.payload or ())
    rv['status'] = self.status_code
    rv['message'] = self.message
    return rv