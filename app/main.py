from blacksheep import Application, Request, delete, get, post, put

from app.api.models import Card
from app.db import crud

app = Application()


@get("/")
def home():
    return "Hello, World!"


@get("/cards")
async def get_all_cards() -> list[Card]:
    full_deck = await crud.get_all_cards()

    return full_deck


@get("/cards/{id}")
async def get_card_by_id(id: int):
    card = await crud.get_card_by_id(id)

    return card


@post("/cards")
async def add_card(request: Request):
    new_card = await crud.add_card(await request.json())

    return new_card


@put("/cards/{id}")
async def update_card(id: int, request: Request):
    updated_card = await crud.update_card(await request.json())

    return updated_card


@delete("/cards/{id}")
async def delete_card(id: int):
    result = await crud.delete_card(id)

    return result
