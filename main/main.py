from fastapi import FastAPI
from middlewares import add_middlwares


app = FastAPI()

add_middlwares(app)

@app.get("/")
async def hi():
    return ["Hello Hamid"]