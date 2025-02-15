from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q:Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.put("/items/{item_id}")
def update_item(item_id: int, item:Item):
    return {"item_name": item.name, "item_price": item.price, "item_id": item_id}
