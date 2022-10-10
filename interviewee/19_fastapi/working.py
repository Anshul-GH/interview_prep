from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[str] = None
    brand: Optional[str] = None


app = FastAPI()

# # end point: base_url/end_point
# @app.get("/")
# def home():
#     return {"Data": "Testing"}

# @app.get("/about")
# def about():
#     return {"Data": "About"}

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    },
    2: {
        "name": "Bread",
        "price": 1.99,
        "brand": "WholeWheat"
    },
    3: {
        "name": "Butter",
        "price": 6.99,
        "brand": "Salted"
    },
    4: {
        "name": "Jam",
        "price": 4.99,
        "brand": "Strawberry"
    }
}


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(
                None,
                description="The Id of the item of concern.",
                gt=0)):
    return inventory[item_id]


@app.get("/get-by-name")
def get_item_by_name(*, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item id not found.")


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Item id already exists.")

    # inventory[item_id] = {
    #     "name": item.name,
    #     "brand": item.brand,
    #     "price": item.price
    # }
    inventory[item_id] = item

    return inventory[item_id]


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item id not found.")

    # inventory[item_id].update(item)

    if item.name is not None:
        inventory[item_id].name = item.name
    if item.price is not None:
        inventory[item_id].price = item.price
    if item.brand is not None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]


@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The id for the item to be deletec.")):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item id not found.")

    del inventory[item_id]
    return {"Success": "Item deleted!"}
