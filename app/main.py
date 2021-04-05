from flask import Blueprint, Flask
from app.controllers.auth import auth
from app.controllers.loan import loan

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/api/auth')
app.register_blueprint(loan, url_prefix='/api/loan')

if __name__ == '__main__':
    app.run()
