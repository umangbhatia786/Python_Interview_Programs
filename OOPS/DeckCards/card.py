# This module defines the Card class for representing playing cards.

class Card:
    """A class to represent a playing card.

    Attributes:
        suit (str): The suit of the card.
        value (str): The value of the card.
    """

    def __init__(self, suit, value):
        """Initialize a Card object with a given suit and value.

        Args:
            suit (str): The suit of the card.
            value (str): The value of the card.
        """
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        """Get the suit of the card."""
        return self._suit
    
    @property
    def value(self):
        """Get the value of the card."""
        return self._value
    
    @suit.setter
    def suit(self, suit):
        """Set the suit of the card."""
        self._suit = suit

    @value.setter
    def value(self, value):
        """Set the value of the card."""
        self._value = value

    def __repr__(self):
        """Return a string representation of the card."""
        return f'{self._value} of {self._suit}'
