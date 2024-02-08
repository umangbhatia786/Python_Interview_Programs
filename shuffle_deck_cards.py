import random

def shuffle_deck_of_cards():
    '''
    Shuffle a deck of cards and return it.

    The deck consists of 52 cards, with each card represented as a tuple containing
    a number (1-13) and a card type (Heart, Spade, Club, Diamond).

    Returns:
    list: The shuffled deck of cards.
    '''
    # Define the types of cards
    card_types = ['Heart', 'Spade', 'Club', 'Diamond']

    # Create an empty deck
    deck = list()

    # Populate the deck with cards
    for card in card_types:
        for num in range(1, 14):
            deck.append((num, card))

    # Shuffle the deck
    random.shuffle(deck)

    return deck

# Shuffle the deck of cards
shuffled_deck = shuffle_deck_of_cards()

# Print the top 5 cards from the shuffled deck
print('******** Top 5 cards from the shuffled deck are ************')
for i in range(0, 5):
    print(f'{shuffled_deck[i][0]} of {shuffled_deck[i][1]}')
