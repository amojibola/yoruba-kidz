from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_health_check():
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.json()["ok"] is True
