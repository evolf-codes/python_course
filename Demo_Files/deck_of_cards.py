import pprint

cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits = ['SPADES','HEARTS','DIAMONDS','CLUBS']

deck_1 = [{}.fromkeys(['SPADES'],x) for x in cards]
deck_2 = [{}.fromkeys(['HEARTS'],x) for x in cards]
deck_3 = [{}.fromkeys(['DIAMONDS'],x) for x in cards]
deck_4 = [{}.fromkeys(['CLUBS'],x) for x in cards]

decks=[deck_1,deck_2,deck_3,deck_4]
deck_main=[]

for each in decks:
    for card in each:
        deck_main.append(card)

# for x in deck_2:
#     deck_main.append(x)
#
# for x in deck_3:
#     deck_main.append(x)
#
# for x in deck_4:
#     deck_main.append(x)

pprint.pprint(deck_main)

