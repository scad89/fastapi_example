from datetime import datetime
from typing import Optional

from typing import Optional

from fastapi_users import models


class User(models.BaseUser):
    id: int
    date_free: Optional[datetime]

    class Config:
        orm_mode = True


class UserCreate(User, models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass


# from datetime import datetime
# import uuid

# from fastapi_users import schemas

# from typing import Optional


# class UserRead(schemas.BaseUser[uuid.UUID]):
#     date_free: Optional[datetime]


# class UserCreate(schemas.BaseUserCreate):
#     date_free: Optional[datetime]


# class UserUpdate(schemas.BaseUserUpdate):
#     date_free: Optional[datetime]
