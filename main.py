from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

from typing import Union

# app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello World": "Main landing page"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
 