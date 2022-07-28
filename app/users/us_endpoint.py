from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from .us_db_controllers import UserRepository
from .us_shemas import User, UserIn
from .us_controllers import get_user_repository, get_current_user


user = APIRouter()


@user.get("/", response_model=List[User])
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 0):
    return await users.get_all(limit=limit, skip=0)


@user.post("/", response_model=User)
async def create_user(
        user: UserIn,
        users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)


@user.put("/", response_model=User)
async def update_user(
        id: int,
        user: UserIn,
        users: UserRepository = Depends(get_user_repository),
        current_user: User = Depends(get_current_user)):
    old_user = await users.get_by_id(id=id)
    if old_user is None or old_user.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return await users.update(id=id, u=user)
