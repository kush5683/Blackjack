class Card:
    def __init__(self, suit: str, value: int | str, hidden: bool=False):
        self.suit: str = suit
        self.value: int | str = value
        self.hidden: bool = hidden

    def __str__(self) -> str:
        if self.hidden:
            return 'Hidden'
        return f'{self.value} of {self.suit}'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def get_value(self) -> int:
        if self.value in ['Jack', 'Queen', 'King']:
            return 10
        elif self.value == 'Ace':
            return 11
        return int(self.value) 
    
    def hide(self) -> 'Card':
        self.hidden = True
        return self
    
    def __add__(self, other: 'Card') -> int:
        my_value: int = self.get_value()
        other_value: int = other.get_value()

        # Handle Ace values
        if my_value == 11 and my_value + other_value > 21:
            my_value = 1
        if other_value == 11 and my_value + other_value > 21:
            other_value = 1
        return my_value + other_value
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.get_value() == other.get_value()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Card):
            return self.get_value() != other.get_value()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Card):
            return self.get_value() < other.get_value()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Card):
            return self.get_value() <= other.get_value()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Card):
            return self.get_value() > other.get_value()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Card):
            return self.get_value() >= other.get_value()
        return NotImplemented
