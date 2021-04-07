from validate_docbr import CPF
from src.repository import ClientsRepository
from src.model.clientes import Client
from datetime import datetime, timedelta
from os import getenv
import src.exceptions as Exceptions
import jwt

cpf_validator = CPF()

class ClientsService:
    def __init__(self):
        self.client_repository = ClientsRepository()

    def create_client(self, body):

        validate_data(body)

        cpf = body['cpf'] if 'cpf' in body else None

        # verify if client is already registered
        if self.client_repository.exists_client(cpf):
            raise Exceptions.AlreadyExistsClientException()

        client = Client(cpf=cpf, nome=body['nome'], celular=body['celular'], negativado=False, score=0)

        # save and get client
        saved_client = self.client_repository.create_client(client)

        return {
            'status': 'Cadastro realizado com sucesso',
            'document_id': str(saved_client)
        }
        
    def auth_client(self, body):
        
        cpf = body['cpf'] if 'cpf' in body else None
        celular = body['celular'] if 'celular' in body else None
        
        if celular is None or cpf is None:
            raise Exceptions.InvalidClientBodyException()
        
        if not self.client_repository.exists_client(cpf):
            raise Exceptions.ClientNotFoundException()
        
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': cpf,
            'celular': celular,
            'cpf': cpf
        }
        try:
            token = jwt.encode(
                payload,
                getenv('SECRET_KEY'),
                algorithm='HS512'
            )
            return { 'status': 'Cliente autorizado', 'token': 'Bearer ' + token }
        except Exception as e:
            raise Exceptions.UnableToAuthException()
        
        
    @staticmethod
    def decode_auth_token(token):
        if token is None or token == '':
            raise Exceptions.UnauthorizedException()
        
        auth_token = token.split(' ')[1]

        try:
            payload = jwt.decode(auth_token, getenv('SECRET_KEY'), algorithms=['HS512'])
            return payload['sub']
        except:
            raise Exceptions.UnauthorizedException()


def validate_data(body):
    # verify if clients body is correctly
    if body is None or body == {}:
        raise Exceptions.InvalidClientBodyException()

    # verify required properties
    valid = True
    for attr, value in body.items():
        if (value is None or value == ''):
            valid = False

    if not valid:
        raise Exceptions.InvalidClientBodyException()

    cpf = body['cpf'] if 'cpf' in body else None
    nome = body['nome'] if 'nome' in body else None
    celular = body['celular'] if 'celular' in body else None

    if (cpf is None or cpf == "" or nome is None or nome == ""
            or celular is None or celular == "" or type(cpf) is not str
            or type(nome) is not str or type(celular) is not str):
        raise Exceptions.InvalidClientBodyException()

    # verify if CPF is valid
    if not cpf_validator.validate(cpf):
        raise Exceptions.InvalidCPFException()