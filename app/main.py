from fastapi import FastAPI
from .database import engine, Base, database
from .routers import posts, reports, users

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(posts.router)
app.include_router(reports.router)
app.include_router(users.router)
