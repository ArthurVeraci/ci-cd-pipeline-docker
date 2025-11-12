from app import app

def test_home_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Flask App rodando em container Docker!" in response.data
