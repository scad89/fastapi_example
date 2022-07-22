from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from core.config import Config

user = APIRouter()

manager = LoginManager(Config.SECRET_KEY, '/login')

DB = Config.SQLALCHEMY_DATABASE_URI


@manager.user_loader()
def query_user(user_id: str):
    return DB['user'].get(user_id)


@user.post('/login')
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = query_user(email)
    if not user:
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data={'sub': email}
    )
    return {'access_token': access_token}
