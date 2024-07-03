from http import HTTPStatus

from fast_zero.schemas import UserPublic
from tests.test_db import TEST_EMAIL, TEST_PASSWORD, TEST_USERNAME


def test_read_root_must_return_ok_and_Hello_World(client):
    # Act (Ação)
    response = client.get('/')

    # Assert (Afirmar)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': TEST_USERNAME,
            'email': TEST_EMAIL,
            'password': TEST_PASSWORD,
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': TEST_USERNAME,
        'email': TEST_EMAIL,
    }

    response = client.post(
        '/users/',
        json={
            'username': TEST_USERNAME,
            'email': TEST_EMAIL,
            'password': TEST_PASSWORD,
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {
        'detail': 'Username already exists',
    }

    response = client.post(
        '/users/',
        json={
            'username': 'new user name',
            'email': TEST_EMAIL,
            'password': TEST_PASSWORD,
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {
        'detail': 'Email already exists',
    }


def test_read_users(client):
    response = client.get('/users/')
    # Vai depender do teste acima, má prática
    # Pelo que entendi os testes são executados em ordem alfabética
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_read_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema

    response = client.get('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'password': TEST_PASSWORD,
            'username': TEST_USERNAME,
            'email': TEST_EMAIL,
            'id': 1,
        },
    )

    assert response.json() == {
        'username': TEST_USERNAME,
        'email': TEST_EMAIL,
        'id': 1,
    }

    response = client.put(
        '/users/2',
        json={
            'password': TEST_PASSWORD,
            'username': TEST_USERNAME,
            'email': TEST_EMAIL,
            'id': 1,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}

    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
