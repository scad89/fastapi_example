from fastapi import APIRouter, HTTPException, status, Depends
from .token_shemas import Token, Login
from ..users.us_db_controllers import UserRepository
from .security import verify_password, create_access_token
from ..users.us_controllers import get_user_repository

auth = APIRouter()


@auth.post("/", response_model=Token)
async def login(login: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")
    return Token(
        access_token=create_access_token({"sub": user.email}),
        token_type="Bearer"
    )
