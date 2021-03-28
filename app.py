import json
from datetime import timedelta
import pyprind
import sys
from flask import Flask, json
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from routes.routes import routes

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'db_credito_express',
    # to run locally
    # 'host': 'localhost',
    'host': 'mongodb://mongo',
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


@app.before_first_request
def inicializa_banco():
    # DELETE ALL
    # User.objects.delete({})

    if User.objects().first() is None:
        print("### ADICIONANDO CLIENTES A BASE DE DADOS ###")
        with open('clientes.json') as f:
            file_data = json.load(f)
        bar = pyprind.ProgBar(int(len(file_data)), bar_char='█', stream=sys.stdout)
        for client in file_data:
            bar.update()
            User(nome=str(client['nome']), cpf=str(client['cpf']), celular=str(client['celular']),
                 score=int(client['score']), negativado=bool(client['negativado'])).save()

    else:
        print("### USANDO BASE DE DADOS EXISTENTE ###")


app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
