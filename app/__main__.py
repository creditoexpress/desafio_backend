import logging
logging.getLogger().setLevel( logging.INFO )

from flask import Flask

def init_app( app ):
    #Database
    from repository import init_db
    init_db()

    #Rotas
    from routes import init_routes
    init_routes( app )
        
    app.run( host = "0.0.0.0", port = 3333 )


if __name__ == '__main__':
    app = Flask(__name__)
    init_app( app )
