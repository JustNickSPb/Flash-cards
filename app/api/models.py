from dataclasses import dataclass


@dataclass
class Card:
    id: int
    question: str
    answer: str
    