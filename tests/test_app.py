from http import HTTPStatus


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
            'username': 'testusername',
            'email': 'test@email.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@email.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    # Vai depender do teste acima, má prática
    # Pelo que entendi os testes são executados em ordem alfabética
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'testusername',
                'email': 'test@email.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': 'password',
            'username': 'testuser',
            'email': 'test@email.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testuser',
        'email': 'test@email.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
