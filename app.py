import json
from datetime import timedelta
from flask import Flask, request, json, Response
from flask_mongoengine import MongoEngine
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
import requests

from utils.taxas import taxas

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'db_credito_express',
    # to run locally
    'host': 'localhost',
    # 'host': 'mongodb://mongo',
    'port': 27017
}
app.config["JWT_SECRET_KEY"] = "credito_express-secret-matheus"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=5)
jwt = JWTManager(app)
db = MongoEngine()
db.init_app(app)


class User(db.Document):
    _id = db.ObjectIdField()
    nome = db.StringField()
    cpf = db.StringField()
    celular = db.StringField()
    score = db.IntField()
    negativado = db.BooleanField()

    def to_json(self):
        return {"_id": str(self._id),
                "nome": self.nome,
                "cpf": self.cpf,
                "celular": self.celular,
                "score": self.score,
                "negativado": self.negativado}


def inicializa_banco():
    # # DELETE ALL
    # User.objects.delete({})

    if User.objects().first() is None:
        print("### ADICIONANDO CLIENTES A BASE DE DADOS ###")
        with open('clientes.json') as f:
            file_data = json.load(f)
        for client in file_data:
            User(nome=str(client['nome']), cpf=str(client['cpf']), celular=str(client['celular']),
                 score=int(client['score']), negativado=bool(client['negativado'])).save()
    else:
        print("### USANDO BASE DE DADOS EXISTENTE ###")


inicializa_banco()


@app.route("/login", methods=['POST'])
def login():
    data = request.json

    if data is None or data == {}:
        return Response(response=json.dumps({"message": "Por favor informe os campos"}),
                        status=400,
                        mimetype='application/json')

    cpf = str(data['cpf'])
    celular = str(data['celular'])

    user = User.objects(cpf=cpf, celular=celular).first()
    access_token = create_access_token(identity=str(user._id))

    return Response(
        content_type="application/json",
        response=json.dumps({
            "user": user.to_json(),
            "token": access_token
        }),
        status=200,
    )


@app.route("/simular", methods=['POST'])
@jwt_required()
def simular_emprestimo():
    data = request.json

    if data is None or data == {}:
        return Response(response=json.dumps({"message": "Por favor informe os campos"}),
                        status=400,
                        mimetype='application/json')

    current_user_id = get_jwt_identity()

    user = User.objects(_id=current_user_id).first()

    valor = data['valor']
    n_parcelas = data['numeroParcelas']

    # negativado
    if user.negativado:
        taxa_juros = taxas[0]['taxas'][str(n_parcelas)]
        print("TAXA DE JUROS APLICADA: " + str(taxa_juros) + "\nTIPO: " + str(taxas[0]['tipo']))
    # alto
    elif user.score > 500:
        taxa_juros = taxas[1]['taxas'][str(n_parcelas)]
        print("TAXA DE JUROS APLICADA: " + str(taxa_juros) + "\nTIPO: " + str(taxas[1]['tipo']))
    # baixo
    else:
        taxa_juros = taxas[2]['taxas'][str(n_parcelas)]
        print("TAXA DE JUROS APLICADA: " + str(taxa_juros) + "\nTIPO: " + str(taxas[2]['tipo']))

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


@app.route("/users", methods=['GET'])
@jwt_required()
def index():
    users = [user.to_json() for user in User.objects()]

    print("QUANTIDADE DE CLIENTES: " + str(len(users)))

    return Response(
        content_type="application/json",
        response=json.dumps({"users": users}),
        status=200,
    )


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
