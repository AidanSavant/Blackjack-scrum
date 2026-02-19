from models.card import Card
from models.hand import Hand
from models.dealer import Dealer
from models.deck import Deck

import pytest

class TestCard:
    def test_values_number_card(self):
        card = Card("5")
        assert card.values == (5, None)

    def test_values_face_card(self):
        card = Card("king")
        assert card.values == (10, None)

    def test_values_ace_card(self):
        card = Card("ace")
        assert card.values == (1, 11)

class TestHand:
    def test_is_blackjack_true(self):
        hand = Hand()
        hand.add_card(Card("ace"))
        hand.add_card(Card("king"))
        assert hand.is_blackjack == True

    def test_is_blackjack_false(self):
        hand = Hand()
        hand.add_card(Card("5"))
        hand.add_card(Card("king"))
        assert hand.is_blackjack == False

class TestDealer:
    def test_has_to_hit_true(self):
        deck = Deck()
        dealer = Dealer(deck)
        dealer.hand = Hand()
        dealer.hand.add_card(Card("10"))
        dealer.hand.add_card(Card("6"))
        assert dealer.has_to_hit() == True

    def test_has_to_hit_false(self):
        deck = Deck()
        dealer = Dealer(deck)
        dealer.hand = Hand()
        dealer.hand.add_card(Card("10"))
        dealer.hand.add_card(Card("7"))
        assert dealer.has_to_hit() == False


if __name__ == "__main__":
    pytest.main()