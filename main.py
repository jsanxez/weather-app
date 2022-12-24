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

@app.get("/weather/", response_class=HTMLResponse)
async def get_zipcode_weather(request: Request, zipcode: str):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{default_country}&units=metric&appid={api_key}")
    weather_data = weather_data.json()
    requested_weather = {"city": weather_data['name'],
                          "temperature": weather_data['main']['temp'],
                          "description": weather_data['weather'][0]['description'],
                          "humidity": weather_data['main']['humidity'],
                          "wind": weather_data['wind']['speed'],
                          }
    return templates.TemplateResponse("index.html", {"request": request, "weather": requested_weather})

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

