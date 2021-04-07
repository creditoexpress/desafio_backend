class InvalidLoanBodyException(Exception):

  def __init__(self, payload=None):
    Exception.__init__(self)
    self.message = 'Informe os dados corretamente (cpf, valor e número de parcelas: 6, 12, 18, 24 ou 36)'

    self.status_code = 400
    self.payload = payload
    
  def to_dict(self):
    rv = dict(self.payload or ())
    rv['status_code'] = self.status_code
    rv['message'] = self.message
    return rv