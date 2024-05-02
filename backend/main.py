from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return 


@app.post("/predictor")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}