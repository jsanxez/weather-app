from typing import Union
import requests

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

api_key = "655dfc390726be35679ee1f171b45301"
default_country = 'us'

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None]=None


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/{zipcode}")
async def get_zipcode_weather(zipcode: str):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{default_country}&appid={api_key}")
    requested_weather = weather_data.json()
    return requested_weather

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

