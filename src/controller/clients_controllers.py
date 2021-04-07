from flask import Blueprint, request, jsonify
from src.service import ClientsService

clients_routes = Blueprint('clients_routes', __name__)

@clients_routes.route('/', methods=['POST'])
def create_client():
    result = ClientsService().create_client(request.json)
    return jsonify(result)

@clients_routes.route('/auth', methods=['POST'])
def auth_client():
    result = ClientsService().auth_client(request.json)
    return jsonify(result)