from validate_docbr import CPF
from flask import json
import src.repository as Repositories
import src.exceptions as Exceptions
import requests

cpf_validator = CPF()

class LoanService:
    
    def __init__(self):
        self.clients_repository = Repositories.ClientsRepository()
        self.fees_repository = Repositories.FeesRepository()
        
    def get_simulation(self, body):
        
        validate_data(body)
        
        cpf = body['cpf'] if 'cpf' in body else None
        valor = body['valor'] if 'valor' in body else None
        numeroParcelas = body['numeroParcelas'] if 'numeroParcelas' in body else None
        
        # verify if client exists
        if not self.clients_repository.exists_client(cpf):
            raise Exceptions.ClientNotFoundException()
        
        # get client by CPF
        client = self.clients_repository.get_client_by_cpf(cpf)
        
        # verify if client with informed CPF is registered
        if client is None or client == {}:
            raise Exceptions.ClientNotFoundException()
    
        # get fee by type
        fee_type = get_client_fee_type(client)
        fee = self.fees_repository.get_fee_by_type(fee_type)
        
        # get client fee and simulation
        client_fee = fee[str(numeroParcelas)]

        payload = { 'numeroParcelas': numeroParcelas, 'valor': valor, 'taxaJuros': client_fee }
        
        req = request_simulation(payload)
        return req.json()

def request_simulation(payload):
    return requests.post('https://us-central1-creditoexpress-dev.cloudfunctions.net/teste-backend', json=payload, headers={'Content-type': 'application/json'})

def validate_data(body):
    
    # verify if fee body is correctly
    if body is None:
        raise Exceptions.InvalidLoanBodyException()
    
    # verify required fields
    valid = True 
    for attr, value in body.items():
        if (value is None or value == ''):
            valid = False
        
    if not valid:
        raise Exceptions.InvalidLoanBodyException()
    
    cpf = body['cpf'] if 'cpf' in body else None
    valor = body['valor'] if 'valor' in body else None
    numeroParcelas = body['numeroParcelas'] if 'numeroParcelas' in body else None
    
    if (cpf is None or cpf == "" or valor is None or valor == "" or numeroParcelas is None or numeroParcelas == ""
        or type(cpf) is not str or (type(valor) is not int and type(valor) is not float) or type(numeroParcelas) is not int or not validate_installments(numeroParcelas)):
      raise Exceptions.InvalidLoanBodyException()
  
    # verify if CPF is valid
    if not cpf_validator.validate(cpf):
        raise Exceptions.InvalidCPFException() #EXCEPTION
    
def validate_installments(installments):
    valid_list = [6, 12, 18, 24, 36]
    return installments in valid_list

def get_client_fee_type(client):
    if client['negativado'] is True:
        return 'NEGATIVADO'
        
    if client['score'] <= 500:
        return 'SCORE_BAIXO'
        
    return 'SCORE_ALTO'