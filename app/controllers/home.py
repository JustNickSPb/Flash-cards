import random

from blacksheep import Request, Response
from blacksheep.server.controllers import Controller, get, route

from app import models
from app.dependencies import get_db
from domain.db.crud import add_card, get_all_cards
from domain.db.db import SessionLocal
from domain.db.models import Card


class Cards(Controller):
    @get()
    def index(self):
        return self.view()

    @route("/add-card", methods=["GET","POST"])
    async def add_card(self, request: Request) -> Response:
        if request.method == "GET":
            return self.view("add")
        form = await request.form()
        card_data = Card(question=form["question"], answer=form["answer"])
        db = SessionLocal()
        add_card(db, card_data)
        return self.view("index")

    @get("/random-card")
    async def random_card(self):
        db = SessionLocal()
        cards = get_all_cards(db)
        random_card = random.choice(cards)
        return self.view("random", model=models.Card(question=random_card.question, answer=random_card.answer))
