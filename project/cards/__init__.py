import random

class Card:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

class Deck:
    """ Stores information about a deck of flashcards. """
    def __init__(self, name, cards=None):
        self.name = name

        if cards == None:
            self.cards = []
        else:
            self.cards = cards

    def add_card(self, side_a, side_b):
        self.cards.append(Card(side_a, side_b))

    def draw_random(self, number_of_cards):
        if number_of_cards > len(self.cards):
            raise IndexError("Number of cards drawn is greater than number of cards in deck")

        elif number_of_cards == len(self.cards):
            cards_drawn = self.cards.copy()
            random.shuffle(cards_drawn)

        else:
            cards_drawn = []
            draw_indices = random.sample(range(len(self.cards)), number_of_cards)

            for i in draw_indices:
                cards_drawn.append(self.cards[i])

        return cards_drawn

