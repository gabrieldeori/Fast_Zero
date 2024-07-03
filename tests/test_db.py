from fast_zero.models import User

def test_create_user():
    user = User(username='test', email='test@test.com', password='secret')

    assert user.username == 'test'
    assert user.email == 'test@test.com'
    assert user.password == 'secret'
