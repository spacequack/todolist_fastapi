from http import HTTPStatus

from fastapi import FastAPI

from todolist_fastapi.routers import auth, users
from todolist_fastapi.schemas import Message

app = FastAPI(title='ToDo List')

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
