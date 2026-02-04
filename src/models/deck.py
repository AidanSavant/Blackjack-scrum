import random

from .card import Card
from typing import Final

CARD_RANKS: Final[list[str]] = [
    "ace",
    *[str(num) for num in range(2, 11)],
    "jack",
    "queen",
    "king"
]

class Deck:
    def __init__(self) -> None:
        self.deck: list[Card] = []
        self.shuffle_deck()

    def shuffle_deck(self) -> None:
        self.deck = [Card(rank) for rank in random.choices(CARD_RANKS, k=52)]

    def deal_card(self) -> Card:
        return self.deck.pop()

