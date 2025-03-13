from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Ola, este e um exemplo de aplicacao Python para CI/CD!" in response.data