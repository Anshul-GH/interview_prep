from fastapi import FastAPI
from pydantic import BaseModel

fapiapp = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = None
    item_id: int

@fapiapp.post("/items/")
def create_item(item: Item):
    return {"item": item}

@fapiapp.get("/items/{item_id}")
def read_item(item_id: int, name: str | None = None, description: str | None = None, price: float | None = None, tax: float | None = None):
    return {"item_id": item_id, "name": name, "description": description, "price": price, "tax": tax}
