from player import Player
from minimax import maxn

class Bot(Player):
    def __init__(self, name) -> None:
        super().__init__(name)

    def think(self) -> None:
        maxn(5)
