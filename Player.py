from Card import Card
class Player:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.hand_soft = False
        self.bet = 0

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
    
    def calculate_hand(self) -> int:
        hand = sorted(self.hand)
        hand_value = 0
        for card in hand:
            wrapper_card = Card(suit="Custom", value=hand_value)
            hand_value = card + wrapper_card
        return hand_value

