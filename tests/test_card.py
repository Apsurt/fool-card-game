from src.card import StandardCard

def test_card():
    card = StandardCard("Spades", "A")
    assert card.suit == "Spades"
    assert card.rank == "A"
    assert card.value == 14
