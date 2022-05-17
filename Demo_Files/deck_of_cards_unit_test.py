import unittest
from deck_of_cards import Card, Deck
#from ddt import ddt, data


class Tests(unittest.TestCase):
    def setUp(self):
        self.c = Card("Hearts","A")
        self.d = Deck()

    def test_repr(self):
        self.assertEqual(str(self.c), 'A of Hearts')

    def test_init(self):
        self.assertEqual(self.c.value,"A")
        self.assertEqual(self.c.suit,"Hearts")

    def test_deck_init(self):
        """the total cards in the deck is 52"""
        self.assertEqual(self.d.total_cards,52)
        self.assertEqual(len(self.d.cards),52)




if __name__ == "__main__":
    unittest.main()
