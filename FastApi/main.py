
from fastapi import FastAPI, Query
from typing import Union

import requests

app = FastAPI()


@app.get("/")
async def read_root():
    var = requests.get("https://jsonplaceholder.typicode.com/todos/1").json()
    return {"saludo": "Hola", "res": var,}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
