from Card import Card
class Player:
    def __init__(self):
        self.hand: list[Card] = []
        self.hand_value: int = 0
        self.hand_soft: bool = False
        self.bet: int = 0
        self.balance: float = 1000

    def hit(self, card: Card):
        self.hand.append(card)
        self.hand_value = self.calculate_hand()
        if card.value == 11:
            self.hand_soft = True
        if self.hand_value > 21 and self.hand_soft:
            self.hand_value -= 10
            self.hand_soft = False
        if self.hand_value == 21:
            return
        
    def place_bet(self, bet: int) -> float:
        self.bet = bet
        self.balance -= bet
        return self.balance
    
    def calculate_hand(self) -> int:
        hand = sorted(self.hand)
        hand_value = 0
        for card in hand:
            wrapper_card = Card(suit="Custom", value=hand_value)
            hand_value = card + wrapper_card
        return hand_value

