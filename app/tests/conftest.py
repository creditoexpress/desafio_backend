import pytest 
from src.app import create_app

@pytest.fixture(scope="module")
def app():
    """Instancia da classe main app flask"""
    return create_app()


