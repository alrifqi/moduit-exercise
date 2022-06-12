from fastapi import FastAPI

from routers.main import main_router

app = FastAPI()

app.include_router(main_router, tags=["question"])
