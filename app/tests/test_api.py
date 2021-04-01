import json
from src.ext.nosql import nosql


def test_function(app):
    assert app.name == 'src.app'
    
    
def test_get_close_db(client,app):
    assert client.get('/findClient').status_code == 200
    response = client.get('/findClient')
    resp = {
        "message": "cpf or celular is required",
        "status": True
    }
    assert json.loads(response.data) == resp


def test_get_cliente(client,app):
    db = nosql.init_app(app)

    assert client.get('/findClient?cpf=19867230540').status_code == 200

    response = client.get('/findClient?cpf=19867230540')
    
    a = db.clientes.find_one({"cpf" : "19867230540"})
    
    response = json.loads(response.data)
    
    assert a['score'] == response['data']['score']
    



def test_post_simulacao(client,app):
    assert client.post('/simular', data={"numeroParcelas": 12,"valor": 10000}).status_code == 200
    
    req = {"numeroParcelas": 12,"valor": 10000}

    response = client.post('/simular', data=json.dumps(req), headers={"Content-Type": "application/json"},)
    response = json.loads(response.data)
    valorParc = response['data']['valorParcela']
    assert valorParc == 862.5