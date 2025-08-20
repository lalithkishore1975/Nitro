from fastapi import FastAPI
from . import models
from .database import engine
from .routes import files

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="File Parser CRUD API")

app.include_router(files.router, prefix="/files", tags=["Files"])
