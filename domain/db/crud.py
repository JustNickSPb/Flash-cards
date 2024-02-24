from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from domain.db.models import Card


def add_card(db: Session, card: Card):
    query = insert(Card).values(question=card.question, answer=card.answer)
    card = db.execute(query)
    db.commit()

    return card


def get_all_cards(db: Session):
    query = select(Card)
    deck = db.execute(query).scalars().all()

    return deck
