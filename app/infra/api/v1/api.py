from ...app_factory import create_app
from .auth_api import router as auth_api
from .simulations import app as simulation_api


app = create_app()

app.include_router(auth_api)

app.mount('/simulate', simulation_api)
