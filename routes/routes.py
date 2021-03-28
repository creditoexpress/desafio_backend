from flask import Blueprint, json, Response, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from utils.taxas import taxas
import requests

VERSION_API = "/v1"

routes = Blueprint('Rotas da api', __name__)


@routes.route(VERSION_API + "/login", methods=['POST'])
def login():
    from app import User

    data = request.json

    try:
        cpf = str(data['cpf'])
        celular = str(data['celular'])
    except (IndexError, KeyError):
        return Response(response=json.dumps({"msg": "Por favor informe os campos."}),
                        status=400,
                        mimetype='application/json')

    user = User.objects(cpf=cpf, celular=celular).first()

    if not user:
        return Response(response=json.dumps({"msg": "CPF ou Celular incorreto. Tente novamente."}),
                        status=401,
                        mimetype='application/json')

    access_token = create_access_token(identity=str(user._id))

    return Response(
        content_type="application/json",
        response=json.dumps({
            "user": user.to_json(),
            "token": access_token
        }),
        status=200,
    )


@routes.route(VERSION_API + "/simular", methods=['POST'])
@jwt_required()
def simular_emprestimo():
    from app import User
    data = request.json
    try:
        valor = float(data['valor'])
        n_parcelas = int(data['numeroParcelas'])
    except (IndexError, KeyError):
        return Response(response=json.dumps({"msg": "Por favor informe os campos."}),
                        status=400,
                        mimetype='application/json')

    try:
        current_user_id = get_jwt_identity()

        user = User.objects(_id=current_user_id).first()

        if not (n_parcelas == 6 or n_parcelas == 12 or n_parcelas == 18 or n_parcelas == 24 or n_parcelas == 36):
            return Response(response=json.dumps({"msg": "Por favor informe uma quantidade de parcelas valida."}),
                            status=400,
                            mimetype='application/json')
        # negativado
        if user.negativado:
            taxa_juros = taxas[0]['taxas'][str(n_parcelas)]
        # alto
        elif user.score > 500:
            taxa_juros = taxas[1]['taxas'][str(n_parcelas)]
        # baixo
        else:
            taxa_juros = taxas[2]['taxas'][str(n_parcelas)]

        endpoint = "https://us-central1-creditoexpress-dev.cloudfunctions.net/teste-backend"

        body = {
            "valor": valor,
            "numeroParcelas": n_parcelas,
            "taxaJuros": taxa_juros
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(endpoint, json=body, headers=headers)

        return Response(
            content_type="application/json",
            response=json.dumps(response.json()),
            status=200,
        )
    except (IndexError, KeyError):
        return Response(response=json.dumps({"msg": "Ocorreu um erro interno no servidor."
                                                    " Tente novamente mais tarde"}),
                        status=500,
                        mimetype='application/json')


@routes.route(VERSION_API + '/users', methods=['GET'])
@jwt_required()
def index():
    from app import User
    try:
        users = [user.to_json() for user in User.objects()]
    except (IndexError, KeyError):
        return Response(response=json.dumps({"msg": "Ocorreu um erro interno no servidor."
                                                    " Tente novamente mais tarde"}),
                        status=500,
                        mimetype='application/json')

    return Response(
        content_type="application/json",
        response=json.dumps({"users": users}),
        status=200,
    )
