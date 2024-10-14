from Card import Card
from random import shuffle
class Shoe:
    def __init__(self, decks_in_shoe: int=6):
        self.decks_in_shoe: int = decks_in_shoe
        self.cards: list[Card] = []
        self.build()
        self.shuffle()

    def build(self):
        for _ in range(self.decks_in_shoe):
            for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                for value in range(2, 11):
                    self.cards.append(Card(suit, value))
                for face in ['Jack', 'Queen', 'King', 'Ace']:
                    self.cards.append(Card(suit, face))

    def shuffle(self):
        shuffle(self.cards)
    
    def deal(self, hidden: bool=False) -> Card:
        return self.cards.pop().hide() if hidden else self.cards.pop()