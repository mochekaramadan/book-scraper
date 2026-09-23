from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data