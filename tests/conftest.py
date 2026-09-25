import pytest
from fastapi.testclient import TestClient

from app.main import app

@pytest.fixture(autouse=True)
def clear_users():
    users.clear()  # Clear the users list before each tes
    
@pytest.fixture
def client():
    return TestClient(app)

     