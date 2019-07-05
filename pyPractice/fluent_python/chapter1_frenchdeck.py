import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Frenchdeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


deck = Frenchdeck()
print(len(deck))
k = choice(deck)
print(k)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = Frenchdeck.ranks.index(card.rank)
    aaa =rank_value * len(suit_values) + suit_values[card.suit]
    return aaa

for card in sorted(deck,key=spades_high):
    print(card)



