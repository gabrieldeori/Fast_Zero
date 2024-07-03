from sqlalchemy import select

from fast_zero.models import User

TEST_USERNAME = 'test'
TEST_EMAIL = 'test@test.com'
TEST_PASSWORD = 'P@55w0rd'


def test_class_create_user():
    user = User(
        username=TEST_USERNAME, email=TEST_EMAIL, password=TEST_PASSWORD
    )

    assert user.username == TEST_USERNAME
    assert user.email == TEST_EMAIL
    assert user.password == TEST_PASSWORD


def test_create_user(session):
    # engine = create_engine('sqlite:///database.db')
    user = User(
        username=TEST_USERNAME, email=TEST_EMAIL, password=TEST_PASSWORD
    )

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == TEST_EMAIL))

    assert result.username == TEST_USERNAME
