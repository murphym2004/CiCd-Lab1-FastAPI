import pytest
from fastapi.testclient import TestClient

from app.main import app,users

@pytest.fixture(autouse=True)
def clear_users():
    users.clear()  # Clear the users list before each test
    
@pytest.fixture
def client():
    return TestClient(app)

     