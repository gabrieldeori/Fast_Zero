from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserSchema, UserPublic, UserDB

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World!'}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):

    # breakpoint() # Para a aplicação ('l' mostra a linha, 'q' sai do debug)

    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump() # Transforma dado em dicionário, e o ** faz tipo o ... do js
    )

    database.append(user_with_id)

    return user_with_id
