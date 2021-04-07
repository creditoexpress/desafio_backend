from flask import Blueprint, request, jsonify
from src.service import LoanService

loan_routes = Blueprint('loan_routes', __name__)

@loan_routes.route('/', methods=['POST'])
def get_simulation():
    result = LoanService().get_simulation(request.json)
    return jsonify(result)