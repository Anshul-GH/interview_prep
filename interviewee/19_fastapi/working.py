from fastapi import FastAPI, Path
from typing import Optional

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
def get_item(item_id: int = Path(None, description="The Id of the item of concern.", gt=0, lt=2)):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(*, name: Optional[str]=None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    
    return {"Data": "Not found .. "}
