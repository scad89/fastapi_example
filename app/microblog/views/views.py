from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.schemas import PostCreate, PostList
from core.utils.get_db import get_db
from ..controllers.api_contollers import PostApiController

api = APIRouter()


@api.get("/", response_model=List[PostList])    # list all responce
def post_list(db: Session = Depends(get_db)):
    return PostApiController.get_post_list(db)


@api.post("/")
def post_list(item: PostCreate, db: Session = Depends(get_db)):
    return PostApiController.create_post(db, item)
