from Shoe import Shoe
from Player import Player
from Card import Card


class Dealer(Player):
    def __init__(self, decks_in_shoe=6):
        super().__init__()
        self.decks_in_shoe = decks_in_shoe
        self.shoe = Shoe(decks_in_shoe)
        self.shoe.shuffle()

    def deal (self, hidden=False) -> Card:
        return self.shoe.deal(hidden=hidden)
    

    