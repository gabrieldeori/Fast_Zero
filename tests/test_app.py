from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_must_return_ok_and_Hello_World():
    # Arrange (Organização)
    client = TestClient(app)

    # Act (Ação)
    response = client.get('/')

    # Assert (Afirmar)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email:': 'user@example.com',
            'password': 'password',
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    # assert response.json() == {
    #     'id': 1,
    #     'username': 'testusername',
    #     'email:': 'user@example.com',
    # }
