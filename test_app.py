from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_chat_oi():
  response = client.post(
    "/chat",
    json={"user": "Test User", "message": "oi"}
  )
  assert response.status_code == 200
  assert response.json() == {"bot": "Olá Test User, tudo bem?"}

def test_chat_other_message():
  response = client.post(
    "/chat", 
    json={"user": "Test User", "message": "hello"}
  )
  assert response.status_code == 200
  assert response.json() == {"bot": "Desculpe, só sei responder 'oi'"}

def test_chat_invalid_body():
  response = client.post(
    "/chat",
    json={"invalid": "data"}
  )
  assert response.status_code == 422