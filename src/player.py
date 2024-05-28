"""
Module for storing player information in Player class.
"""

from typing import List
import pyCardDeck
from pyCardDeck import CardType

class Player:
    """
    Class for player data.
    """
    def __init__(self, name) -> None:
        self.name = name
        self.hand = pyCardDeck.Deck([], False, f"Hand of {self.name}")

    def get_cards(self) -> List[CardType]:
        """
        Get cards in hand.

        :return: cards in hand.
        :rtype: List[CardType]
        """
        return list(iter(self.hand))

    def draw(self, card: CardType) -> None:
        """
        Adds card to hand.

        :param card: card to add.
        :type card: CardType
        """
        self.hand.add_single(card)

    @property
    def cards_left(self) -> int:
        """
        Number of cards in hand.

        :return: number of cards in hand.
        :rtype: int
        """
        return self.hand.cards_left

    def print_hand(self) -> None:
        """
        Prints cards in hand.
        """
        print(self.get_cards())

    def get_attacking_sequence(self) -> List[CardType]:
        """
        Returns attacking sequence

        :return: attacking sequence.
        :rtype: List[CardType]
        """
        #placeholder
        return [self.hand.draw()]

    def get_defending_sequence(self, attacking_sequence: List[CardType]) -> List[CardType]:
        """
        Returns defending sequence.

        :param attacking_sequence: attacking sequence to beat.
        :type attacking_sequence: List[CardType]
        :return: defending sequence.
        :rtype: List[CardType]
        """
        #placeholder
        return [None]*len(attacking_sequence)
