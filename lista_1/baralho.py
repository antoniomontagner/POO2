
from random import randint as rand
from random import shuffle

suits = ("Spades","Hearts","Clubs","Diamonds")

class Card:
    def __init__(self, rank, suit):
        if rank not in range(1, 14):
            raise TypeError('Rank must be an integer between 1 and 13.')
        if suit not in suits:
            raise TypeError('Suit must be a string: "Spades", "Hearts", "Clubs", or "Diamonds".')
        # The quick check above makes sure the card being made actually exists in a standard deck of 52.
        # If so, the card is created succesfully.
        self.rank = rank
        self.suit = suit


    def cardName(self):
        """
        Returns a string containing the card's name in common terms.
        """
        if self.rank == 1:
            trueRank = "Ace"
        elif self.rank == 11:
            trueRank = "Jack"
        elif self.rank == 12:
            trueRank = "Queen"
        elif self.rank == 13:
            trueRank = "King"
        else:
            trueRank = str(self.rank)
        return "{rank} of {suit}".format(rank = trueRank, suit = self.suit)

    def flip(self):
        """
        Reveals the requested card.
        """
        print(self.cardName())

def newDeck():
    """
    Resets the deck to ascending order, containing all 52 cards.
    """
    global cardDeck
    cardDeck = [Card(rank, suit) for suit in suits for rank in range(1, 14)]
    cardDeck.reverse() # So that the bottom of the list is the top of the deck, i.e. the Ace of Spades is drawn first by 'cardDeck.pop()'.

print(newDeck())   # To generate the deck at the start. Note that it is not shuffled at first.