"""
Module containing card class
"""

from pyCardDeck import BaseCard
from dictionaries import suits, short_to_value

class StandardCard(BaseCard):
    """
    Class for standard card.
    """
    def __init__(self, suit: str, rank: str, name: str) -> None:
        super().__init__(f"{rank} of {suit}")
        self.suit = suit
        self.rank = rank
        self.value = short_to_value[rank]
        self.is_trump = False

    def __repr__(self) -> str:
        return self.rank+suits[self.suit]

    def __eq__(self, other) -> bool:
        return self.rank == other.rank and self.suit == other.suit

    def __gt__(self, other) -> bool:
        if (self.is_trump) and (other.is_trump):
            return self.value > other.value
        if (self.is_trump) and (not other.is_trump):
            return True
        if (not self.is_trump) and (other.is_trump):
            return False
        if (not self.is_trump) and (not other.is_trump):
            if self.suit != other.suit:
                return False
            return self.value > other.value
        return False
