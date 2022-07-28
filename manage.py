from app import create_app
from core.db import database
import uvicorn


app = create_app()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("manage:app", port=8000, host="0.0.0.0", reload=True)
