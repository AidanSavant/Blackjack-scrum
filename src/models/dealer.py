from .player import Player

class Dealer(Player):
    def has_to_hit(self) -> bool:
        return self.hand.highest_value < 17

