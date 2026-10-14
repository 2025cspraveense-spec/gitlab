
from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Password Generator" in response.data


def test_generate_password():
    client = app.test_client()
    response = client.post("/", data={"length": "12"})
    assert response.status_code == 200
    assert b"Your Password:" in response.data


def test_invalid_length():
    client = app.test_client()
    response = client.post("/", data={"length": "5"})
    assert response.status_code == 200
    assert b"Choose a length between 8 and 64." in response.data

