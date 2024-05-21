import pyCardDeck
from typing import List
from pyCardDeck import CardType

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = pyCardDeck.Deck([], False, f"Hand of {self.name}")

    def draw(self, card: pyCardDeck.CardType) -> None:
        self.hand.add_single(card)

    def print_hand(self) -> None:
        print(self.hand._cards)

    def get_attacking_sequence(self) -> List[CardType]:
        pass

    def get_defending_sequence(self) -> List[CardType]:
        pass