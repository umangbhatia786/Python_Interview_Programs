# Deck of Cards

This project includes classes for representing a standard deck of playing cards.

## Deck Class

The `Deck` class represents a deck of 52 playing cards. It has methods for dealing cards, shuffling the deck, and counting the number of cards in the deck.

### Attributes
- `suit`: List of card suits.
- `value`: List of card values.

### Methods
- `__init__()`: Initializes a deck with all 52 cards.
- `__repr__()`: Returns a string representation of the deck.
- `count()`: Returns the number of cards in the deck.
- `_deal(num)`: Deals a specified number of cards from the deck.
- `deal_card()`: Deals a single card from the deck.
- `deal_hand(num)`: Deals a specified number of cards for a hand.
- `shuffle_cards()`: Shuffles the deck if it's a full deck.

## Card Class

The `Card` class represents an individual playing card with a suit and value.

### Attributes
- `suit`: The suit of the card.
- `value`: The value of the card.
