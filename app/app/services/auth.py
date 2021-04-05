from datetime import datetime, timedelta
from jwt import encode as jwt_encode, decode as jwt_decode
from jwt.exceptions import InvalidTokenError

from app.services.database import Database


class Auth:

    @staticmethod
    def identify(request_data):
        cpf = request_data['cpf']
        celular = request_data['celular']

        db = Database()
        
        cliente = db.select_cliente(cpf,celular)
            
        if cliente:
            payload = {'nome': cliente[0].nome, 
                        'cpf': cliente[0].cpf, 
                        'celular': cliente[0].celular
            }
            token = JWT.encode(payload)
            res = {'status': 200, 'message':'Client successfully identified', 'token': token}
        else:
            payload = {'cpf': cpf,
                        'celular': celular
            }
            token = JWT.encode(payload)
            res = {'status': 200, 'message':'Client successfully identified', 'token': token}

        return res    

class JWT:

    @staticmethod
    def add_jwt_signatures(payload, expiration_days=7):
        
        payload['iat'] = datetime.utcnow()
        payload['exp'] = datetime.utcnow() + timedelta(days=expiration_days)
        payload['sub'] = 'api.creditexpress.com.br'

        return payload

    @staticmethod
    def encode(payload, secret='zn1xct1RFpGvuyXC3E9BreRjVl9x1GxQ', algorithm="HS512"):

        payload = JWT.add_jwt_signatures(payload)
        encoded = jwt_encode(payload, secret, algorithm=algorithm).decode('utf-8')

        return encoded
    
    @staticmethod
    def decode(encoded, secret='zn1xct1RFpGvuyXC3E9BreRjVl9x1GxQ', algorithm="HS512"):

        try:
            decoded = jwt_decode(encoded, secret, algorithm=algorithm)
        except InvalidTokenError as error:
            decoded = False

        return decoded
