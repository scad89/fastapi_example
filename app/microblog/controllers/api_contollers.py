from ..schemas.schemas import PostCreate
from .db_contollers import PostDBController
from sqlalchemy.orm import Session


class PostApiController:
    @classmethod
    def get_post_list(cls, db: Session):
        return PostDBController.get_all_post(db)

    @classmethod
    def create_post(cls, db: Session, item: PostCreate):
        return PostDBController.create_post_db(db, item)
