import datetime
from typing import List, Optional
from .us_models import users
from .us_shemas import User, UserIn
from ..base_repository import BaseRepository
from app.auth.security import hash_password


class UserRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)    # обращаемся к базе данных

    async def get_by_id(self, id: int) -> Optional[User]:
        query = users.select().where(users.c.id == id)
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return User.parse_obj(user)    # возвращает из объект дб в объект User

    async def create(self, u: UserIn) -> User:
        user = User(
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**user.dict()}    # передаём значения модели в словарь
        values.pop("id", None)    # удаляем id из словаря
        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update(self, id: int, u: UserIn) -> User:
        user = User(
            id=id,    # user.id = await не делаем, так как есть в самом начале
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password2),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        query = users.update().where(users.c.id == id).values(**values)
        await self.database.execute(query)
        return user

    async def get_by_email(self, email: str) -> User:
        query = users.select().where(users.c.email == email)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)
