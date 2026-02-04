from .card import Card

from dataclasses import dataclass, field

@dataclass(slots=True)
class Hand:
    cards: list[Card] = field(default_factory=list)

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    @property
    def possible_values(self) -> list[int]:
        totals: set[int] = {0}

        for card in self.cards:
            new_totals: set[int] = set()

            for total in totals:
                lhv, rhv = card.values

                new_totals.add(total + lhv)
                if rhv is not None:
                    new_totals.add(total + rhv)

            # NOTE: Deduplicates as we go
            totals = new_totals

        return sorted(totals)

    @property
    def highest_value(self) -> int:
        return max(
            (value for value in self.possible_values if value <= 21),
            default=min(self.possible_values)
        )

    @property
    def is_blackjack(self) -> bool:
        return self.highest_value == 21

    @property
    def is_bust(self) -> bool:
        return self.highest_value > 21

