import json

import sys, os

from flask import (
	Blueprint, request, session, Response
)

BASE_PATH = os.path.abspath(__file__+ '/../../../../')
sys.path.append(BASE_PATH)

# import class for users
from src.classes.db.Users import Users

UsersBp = Blueprint('users', __name__, url_prefix='/users')

@UsersBp.route('/criar', methods=['POST'])
def criar_um():
	input_json = request.json
	resp       = Users().criar(input_json)
	status     = 200 if resp['ok'] else 400    
	response   = Response(
		response = json.dumps(resp),
		status   = status,
		mimetype = 'application/json'
	)

	return response

@UsersBp.route('/criarMuitos', methods=['POST'])
def criar_many():

	input_json = request.json
	resp       = Users().criar_multiplos(input_json)
	status     = 200 if resp['ok'] else 400 

	response = Response(
		response = json.dumps(resp),
		status   = status,
		mimetype = 'application/json'
	)

	return response

@UsersBp.route('/verificar', methods=['POST'])
def verificar():

	input_json = request.json
	resp       = Users().verificar(input_json)
	status     = 200 if resp['ok'] else 400 

	response = Response(
		response = json.dumps(resp),
		status   = status,
		mimetype = 'application/json'
	)

	return response

@UsersBp.route('/calcularJuros', methods=['POST'])
def calcular_juros():

	input_json = request.json
	resp       = Users().calcular_juros(input_json)
	status     = 200 if resp['ok'] else 400
 
	response = Response(
		response = json.dumps(resp),
		status   = status,
		mimetype = 'application/json'
	)

	return response