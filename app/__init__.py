from fastapi import FastAPI
from starlette.responses import Response
from starlette.requests import Request
from core.db import SessionLocal
from app.microblog.views.views import api
from app.users.views.views import user


def create_app():
    app = FastAPI()

    @app.middleware("http")
    async def db_session_middleware(request: Request, call_next):
        response = Response("Internal server error", status_code=500)
        try:
            request.state.db = SessionLocal()
            response = await call_next(request)
        finally:
            request.state.db.close()
        return response

    app.include_router(api, prefix="/blog")
    app.include_router(user, prefix="/user")

    return app
