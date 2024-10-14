import unittest
from Card import Card

class TestCardAddition(unittest.TestCase):
    def test_add_number_cards(self):
        card1 = Card('Hearts', 5)
        card2 = Card('Diamonds', 6)
        self.assertEqual(card1 + card2, 11)

    def test_add_face_cards(self):
        card1 = Card('Hearts', 'Jack')
        card2 = Card('Diamonds', 'Queen')
        self.assertEqual(card1 + card2, 20)

    def test_add_ace_and_number(self):
        card1 = Card('Hearts', 'Ace')
        card2 = Card('Diamonds', 9)
        self.assertEqual(card1 + card2, 20)

    def test_add_ace_and_face(self):
        card1 = Card('Hearts', 'Ace')
        card2 = Card('Diamonds', 'King')
        self.assertEqual(card1 + card2, 21)

    def test_add_two_aces(self):
        card1 = Card('Hearts', 'Ace')
        card2 = Card('Diamonds', 'Ace')
        self.assertEqual(card1 + card2, 12)

    def test_add_ace_and_number_bust(self):
        card1 = Card('Hearts', 'Ace')
        card2 = Card('Diamonds', 11)
        self.assertEqual(card1 + card2, 12)

    



if __name__ == '__main__':
    unittest.main()
