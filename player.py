"""
Module for storing player information in Player class.
"""

from typing import List
import pyCardDeck
from pyCardDeck import CardType

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = pyCardDeck.Deck([], False, f"Hand of {self.name}")

    def get_cards(self):
        return list(iter(self.hand))

    def draw(self, card: pyCardDeck.CardType) -> None:
        self.hand.add_single(card)

    @property
    def cards_left(self) -> int:
        return self.hand.cards_left

    def print_hand(self) -> None:
        print(self.hand._cards)

    def get_attacking_sequence(self) -> List[CardType]:
        #placeholder
        return [self.hand.draw()]

    def get_defending_sequence(self, attacking_sequence: List[CardType]) -> List[CardType]:
        #placeholder
        return [None]*len(attacking_sequence)
