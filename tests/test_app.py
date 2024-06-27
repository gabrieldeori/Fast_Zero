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
            'username': 'str',
            'email': 'test@email.com',
            'password': 'str',
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    # assert response.json() == {
    #     'id': 1,
    #     'username': 'testusername',
    #     'email:': 'user@example.com',
    # }
