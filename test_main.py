from main import app
from flask import json
import pytest
import os
import logging

LOGGER = logging.getLogger(__name__)

content_type = 'application/json'

@pytest.fixture
def app_client():
    os.environ['DB_USER'] = 'ce_user'
    os.environ['DB_PASS'] = 'znmhVq6ninrBwC6'
    os.environ['DB_HOST'] = 'creditoexpresscluster.uyijj.mongodb.net'
    os.environ['SECRET_KEY'] = 'uSDMmdutBP'
    app_client = app.test_client()
    return app_client

def test_create_client(app_client):
    
    payload = {
        'nome': 'Fabio Erickson',
        'cpf': '90381930092',
        'celular': '11992299229'
    }
    
    headers = {
        'Content-Type': content_type
    }
    
    LOGGER.info('Requesting POST to create client...')
    
    request = app_client.post('/clients/', data=json.dumps(payload), headers=headers)
    
    assert request.content_type == content_type
    assert 'document_id' in request.json or ('message' in request.json and request.json['message'] == 'Este cliente já está cadastrado')
    
    LOGGER.info('Client was created or already exists')
    
def test_auth_client(app_client):
    
    payload = {
        'cpf': '93762814031',
        'celular': '71935228778'
    }
    
    headers = {
        'Content-Type': content_type
    }
    
    LOGGER.info('Requesting POST to authenticate client...')

    request = app_client.post('/clients/auth', data=json.dumps(payload), headers=headers)
    
    assert request.content_type == content_type
    assert 'token' in request.json
    
    LOGGER.info('Client was successfuly authenticated')
    
def test_get_loan(app_client):
    
    auth_payload = {
        'cpf': '93762814031',
        'celular': '71935228778'
    }
    
    auth_headers = {
        'Content-Type': content_type
    }
    
    LOGGER.info('Authenticating client...')
    
    auth_request = app_client.post('/clients/auth', data=json.dumps(auth_payload), headers=auth_headers)
    
    LOGGER.info('Client authenticated')
    
    payload = {
        'cpf': '93762814031',
        'numeroParcelas': 36,
        'valor': 10000
    }
    
    headers = {
        'Content-Type': content_type,
        'Authorization': auth_request.json['token']
    }
    
    LOGGER.info('Requesting POST to get simulation data...')
    
    request = app_client.post('/loans/', data=json.dumps(payload), headers=headers)
    
    response = request.json
    
    assert request.content_type == content_type
    assert 'numeroParcelas' in response
    assert 'outrasTaxas' in response
    assert 'total' in response
    assert 'valorJuros' in response
    assert 'valorParcela' in response
    assert 'valorSolicitado' in response
    
    LOGGER.info('Simulation data was successfuly obtained')