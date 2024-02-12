"""
This module defines a Deck class for a standard deck of cards.

Attributes:
    suit (list): List of card suits.
    value (list): List of card values.

Methods:
    __init__: Initializes a deck with all 52 cards.
    __repr__: Returns a string representation of the deck.
    count: Returns the number of cards in the deck.
    _deal: Deals a specified number of cards from the deck.
    deal_card: Deals a single card from the deck.
    deal_hand: Deals a specified number of cards for a hand.
    shuffle_cards: Shuffles the deck if it's a full deck.
"""

from card import Card
from random import shuffle

class Deck:
    suit = ['Hearts', 'Diamond', 'Club', 'Spade']
    value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

    def __init__(self):
        """Initializes a deck with all 52 cards."""
        self.cards = [Card(s,v) for s in Deck.suit for v in Deck.value]

    def __repr__(self):
        """Returns a string representation of the deck."""
        return f'Deck of {self.count()} cards'
    
    def count(self):
        """Returns the number of cards in the deck."""
        return len(self.cards)
    
    def _deal(self, num):
        """Deals a specified number of cards from the deck."""
        count = self.count()
        actual = min([count, num])

        if count == 0:
            raise ValueError('All cards have been dealt.')

        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]

        return cards
    
    def deal_card(self):
        """Deals a single card from the deck."""
        return self._deal(1)[0]
    
    def deal_hand(self, hand_size):
        """Deals a specified number of cards for a hand."""
        return self._deal(hand_size)
    
    def shuffle_cards(self):
        """Shuffles the deck if it's a full deck."""
        if self.count() < 52:
            raise ValueError('Only full decks can be shuffled.')
        return shuffle(self.cards)
    
my_deck = Deck()
print(my_deck)
print(my_deck.cards)
my_deck.shuffle_cards()
print(my_deck.cards)
card = my_deck.deal_card()
print(card)
hand = my_deck.deal_hand(5)
print(hand)
print(my_deck)
