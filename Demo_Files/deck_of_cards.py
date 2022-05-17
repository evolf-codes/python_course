import pprint
import random


class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck():
    total_cards = 52
    dealt_cards = []

    def __init__(self, cards=[]):
        val = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suit = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self.cards = []
        for x in val:
            self.cards.append(Card( suit[0],x))
            self.cards.append(Card( suit[1],x))
            self.cards.append(Card( suit[2],x))
            self.cards.append(Card( suit[3],x))

    def __repr__(self):
        return f"Deck of {Deck.total_cards} cards"

    def count(self):
        return Deck.total_cards

    def _deal(self, num):
        self.num = num
        end = Deck.total_cards-1

        if Deck.total_cards >= num:
            for x in reversed(range(end-num,end)):
                val = self.cards.pop(x)
                Deck.dealt_cards.append(val)
            Deck.total_cards = Deck.total_cards - num

        elif (Deck.total_cards < num - 1 and Deck.total_cards != 0):
            for x in reversed(range(0, end)):
                val = self.cards.pop(x)
                Deck.dealt_cards.append(val)
            Deck.total_cards = 0

        else:
            raise ValueError("All cards have been dealt")

    def shuffle(self):
        if Deck.total_cards == 52:
            random.shuffle(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")

    def deal_card(self):
        self._deal(1)
        last_card = len(Deck.dealt_cards) -1
        return Deck.dealt_cards[last_card]

    def deal_hand(self,num):
        self.num = num
        self._deal(num)
        last_card = len(Deck.dealt_cards) -1
        return Deck.dealt_cards[last_card-num:last_card]

# b=Deck()
# b.shuffle()
# b._deal(25)
#
# print(Deck.dealt_cards)
# b._deal(1)
# print(Deck.dealt_cards)
# print(b.deal_card())
# print(b.deal_hand(5))










# col_1 = [{}.fromkeys(['SPADES'], x) for x in val]
# col_2 = [{}.fromkeys(['HEARTS'], x) for x in val]
# col_3 = [{}.fromkeys(['DIAMONDS'], x) for x in val]
# col_4 = [{}.fromkeys(['CLUBS'], x) for x in val]
#
# all_52 = [col_1, col_2, col_3, col_4]
# deck_main = []
#
# for x in all_52:
#     for y in x:
#         deck_main.append(y)
#
# random.shuffle(deck_main)
# pprint.pprint(deck_main)

# def __init__(self,cards):


# for x in deck_2:
#     deck_main.append(x)
#
# for x in deck_3:
#     deck_main.append(x)
#
# for x in deck_4:
#     deck_main.append(x)
