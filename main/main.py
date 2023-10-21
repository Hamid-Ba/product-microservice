from fastapi import FastAPI

from app import products
from persistence import models, database
from middlewares import add_middlwares

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

add_middlwares(app)

app.include_router(products.router)