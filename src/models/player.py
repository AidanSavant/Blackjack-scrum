from .hand import Hand
from .deck import Deck

from dataclasses import dataclass

@dataclass(slots=True)
class Player:
    hand: Hand

    def __init__(self, deck: Deck) -> None:
        self.hand = Hand()
        self.hand.add_card(deck.deal_card())
        self.hand.add_card(deck.deal_card())
    
    def hit(self, deck: Deck) -> None:
        self.hand.add_card(deck.deal_card())

