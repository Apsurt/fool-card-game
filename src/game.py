"""
Module handling logic of the game.
"""

from typing import List
import pyCardDeck
from pyCardDeck import CardType
from .card import StandardCard
from .dictionaries import ranks_short_to_long, suits
from .player import Player
from .errors import InvalidMove

def default_cards() -> List[CardType]:
    """
    Creates list of standard playing cards.

    :return: List of cards.
    :rtype: List[CardType]
    """
    cards = []
    for suit in suits:
        for rank, name in ranks_short_to_long.items():
            cards.append(StandardCard(suit, rank, name))
    return cards

class Game:
    """
    Class handling logic and game loop.
    """
    def __init__(self) -> None:
        self.deck = pyCardDeck.Deck(default_cards(), reshuffle=False, name="Deck")
        self.attack_pile = pyCardDeck.Deck([], False, name="Attack pile")
        self.discard_pile = pyCardDeck.Deck([], False, name="Discard pile")
        self.deck.shuffle()

        self.trump = self.deck.draw()
        self.trump_suit = self.trump.suit
        self.trump.is_trump = True

        for card in self.deck._cards:
            if card.suit == self.trump_suit:
                card.is_trump = True

        self.players = []
        self.current_player_idx = 0

    def add_player(self, name: str, player_class: type[Player] = Player) -> None:
        """
        Adds player to list of players.

        :param name: Name of the player to add
        :type name: str
        :param player_class: constructor of a class that inherits from Player, defaults to Player
        :type player_class: type[Player], optional
        """
        self.players.append(player_class(name))

    @property
    def player_count(self) -> int:
        """
        Returns count of players in game.

        :return: Number of players
        :rtype: int
        """
        return len(self.players)

    @property
    def current_player(self) -> Player:
        """
        Returns current player indicated by current_player_idx.

        :return: Current player
        :rtype: Player
        """
        return self.players[self.current_player_idx]

    def get_player(self, player_idx: int) -> Player:
        """
        Returns player at given index from players list.

        :param player_idx: Index of players list
        :type player_idx: int
        :return: Player at index
        :rtype: Player
        """
        return self.players[player_idx]

    def find_player(self, name: str) -> Player:
        """
        Finds player by name in players list.

        :param name: Name of player to find
        :type name: str
        :return: Player with specified name
        :rtype: Player
        """
        for player in self.players:
            if player.name == name:
                return player
        return None

    def advance_current_player(self) -> int:
        """
        Advances current_player_idx to next player.

        :return: Next current_player_idx
        :rtype: int
        """
        self.current_player_idx += 1
        self.current_player_idx %= self.player_count
        return self.current_player_idx

    def player_draw(self, player_idx: int) -> StandardCard:
        """
        Draws card from deck and add it to specified players hand.

        :param player_idx: Drawing player index
        :type player_idx: int
        :return: Drawn card
        :rtype: StandardCard
        """
        drawn_card = self.deck.draw()
        self.players[player_idx].draw(drawn_card)
        return drawn_card

    def player_fill(self, player_idx: int, limit: int = 5) -> None:
        """
        Fills player hand till cretain limit

        :param player_idx: Drawing player index
        :type player_idx: int
        :param limit: fill hand till this number, defaults to 5
        :type limit: int, optional
        """
        while self.get_player(player_idx).cards_left < limit:
            self.player_draw(player_idx)

    def update_players_knowledge(self):
        for player in self.players:
            player.known_cards = {}
            for other in self.players:
                known = set()
                for card in other.get_public_cards():
                    known.add(card)
                player.known_cards[other.name] = known
            discarded = set()
            for card in self.discard_pile:
                discarded.add(card)
            player.known_cards["discard"] = discarded

    def attack(self, sequence: List[CardType]) -> None:
        print("Attacking sequence:")
        print(sequence)
        if self.attack_pile.cards_left:
            raise InvalidMove("Attack pile not empty, defend first.")
        if len(sequence)%2 != 1:
            raise InvalidMove("Attack sequence has to be odd number of cards.")
        rank_set = {card.rank for card in sequence}
        if len(sequence) > 1:
            if len(rank_set) > (len(sequence)+1)/2:
                raise InvalidMove("Pair rule violated.")
        for card in sequence:
            card.is_public = True
        self.attack_pile.add_many(sequence)

    def defend(self, sequence: List[CardType]) -> List[CardType]:
        print("Defending sequence:")
        print(sequence)
        if not self.attack_pile.cards_left:
            raise InvalidMove("Nothing to defend")
        if len(sequence) != self.attack_pile.cards_left:
            raise InvalidMove(
                "Number of cards in sequence has to be equal to number of cards on attack pile.")
        draw_from_attack = []
        for idx, card in enumerate(sequence):
            attack_card = list(iter(self.attack_pile))[idx]
            if not card:
                draw_from_attack.append(attack_card)
            else:
                if card > attack_card:
                    card.is_public = True
                    attack_card.is_public = True
                    self.discard_pile.add_many([card, attack_card])
                else:
                    raise InvalidMove("Defending card weaker or wrong suit.")
        self.attack_pile.clear()
        return draw_from_attack

    def run(self) -> None:
        """
        Main game loop.
        """
        for i in range(self.player_count):
            self.player_fill(i)
            self.get_player(i).print_hand()
        running = True
        while running:
            self.update_players_knowledge()
            for player in self.players:
                print(f"Known_cards for player {player.name}")
                print(player.known_cards)
            player = self.current_player
            if player.cards_left == 0:
                self.advance_current_player()
                continue
            drawn = []
            if self.attack_pile.cards_left:
                seq = player.get_defending_sequence(list(iter(self.attack_pile)))
                drawn = self.defend(seq)
                player.hand.add_many(drawn)
            try:
                self.player_fill(self.current_player_idx)
            except pyCardDeck.OutOfCards:
                pass
            if len(drawn) == 0:
                seq = player.get_attacking_sequence()
                self.attack(seq)
            try:
                self.player_fill(self.current_player_idx)
            except pyCardDeck.OutOfCards:
                pass
            self.advance_current_player()

            #placeholder break
            non_zero_count = 0
            for player in self.players:
                if player.cards_left != 0:
                    non_zero_count += 1
            if non_zero_count == 1:
                running = False

        for i in range(self.player_count):
            self.get_player(i).print_hand()

if __name__ == "__main__":
    game = Game()
    print(repr(game.trump))
    game.add_player("1")
    game.add_player("2")
    game.run()
