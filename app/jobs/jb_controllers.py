from .jb_db_controllers import JobRepository
from core.db import database


def get_job_repository() -> JobRepository:
    return JobRepository(database)
