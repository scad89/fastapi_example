from fastapi import FastAPI
from core.db import metadata, engine
from app.jobs.jb_models import jobs
from app.users.us_models import users
from .users.us_endpoint import user
from .auth.auth_endpoint import auth
from .jobs.jb_endpoint import job


def create_app():
    app = FastAPI(title="Test Project")
    metadata.create_all(bind=engine)

    app.include_router(auth, prefix="/auth", tags=["auth"])
    app.include_router(user, prefix="/users", tags=["users"])
    app.include_router(job, prefix="/job", tags=["job"])

    return app
