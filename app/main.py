from .infra.api.v1.api import app


@app.get('/health')
def get_health():
    return { 'status': 'UP' }
