from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from fast_zero.models import User, table_registry

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


def test_create_user():
    # engine = create_engine('sqlite:///database.db')
    engine = create_engine('sqlite:///:memory:')
    # Dura apenas durante o teste

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            username=TEST_USERNAME, email=TEST_EMAIL, password=TEST_PASSWORD
        )

        session.add(user)
        session.commit()
        # session.refresh(user)

        result = session.scalar(
            select(User).where(User.email == TEST_EMAIL)
        )
        # Query Mapeia e retorna resultado como objeto

    # assert user.id == 1
    assert result.username == TEST_USERNAME
