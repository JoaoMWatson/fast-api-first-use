from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
async def root():
    return {"message":"Hello, cu"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"Item": item_id}


@app.post("/items/")
async def create_item(item: Item):
    return item

