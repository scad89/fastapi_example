from sqlalchemy.orm import Session

from ..schemas.schemas import PostCreate
from ..models.models import Post


class PostDBController:
    @classmethod
    def get_all_post(cls, db: Session):
        return db.query(Post).all()

    @classmethod
    def create_post_db(cls, db: Session, item: PostCreate):
        new_post = Post(**item.dict())
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post
