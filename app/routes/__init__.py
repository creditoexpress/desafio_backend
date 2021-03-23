from .user import user_routes
from .taxa import taxa_routes
from .simulacao_emprestimo import simulacao_emprestimo_routes

def init_routes( app ):
    app.register_blueprint( user_routes )
    app.register_blueprint( taxa_routes )
    app.register_blueprint( simulacao_emprestimo_routes )

    return app