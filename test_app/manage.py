from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author, BookOut
from typing import List

app = FastAPI()


@app.get('/')
def home():
    return {"key": "Hello!"}


# @app.get('/{pk}')
# def get_item(pk: int):
#     return {"key": pk}


@app.get('/test/{pk}')
def get_item_and_str(pk: int, q: str = None):    # http://127.0.0.1:8000/1?q=rr
    return {"key": pk, "q": q}


@app.get('/user/{pk}/item/{item}')
def get_user_item(pk: int, item: str):
    return {"user": pk, "item": item}
    # {"user":2,"item":"hh"}  http://127.0.0.1:8000/user/2/item/hh


# @app.post('/book')
# def create_book(item: Book, author: Author, quantity: int = Body(...)):
#     return {"item": item, "authod": author, "quantity": quantity}


@app.get('/book')
def get_book(q: List[str] = Query(["test", "test2"], description="Search book", deprecated=True)):
    return q


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
    return {"pk": pk, "pages": pages}


@app.post('/author')
def create__author(author: Author = Body(..., embed=True)):
    return {"author": author}


# @app.post('/book', response_model=Book, response_model_exclude=True)
# def create_book(item: Book):
#     return item

# @app.post('/book', response_model=BookOut)
# def create_book(item: Book):
#     # book = item.dict()
#     # book["id"] = 3
#     # return book
#     return BookOut(**item.dict(), id=3)
