import random

from nate.ejercicios.blackjack_UI.card import Card


class Deck:
    suits = ["diamonds", "hearts", "spades", "clubs"]
    max_number = 13

    def __init__(self):
        self.cards = []
        self.used_cards = []

        for suit in self.suits:
            for number in range(1, self.max_number + 1):
                self.cards.append(Card(number, suit))

    def give_random_card(self):
        try:
            pos = random.randint(0, len(self.cards))
            chosen_card = self.cards.pop(pos-1)
            self.used_cards.append(chosen_card)
            return chosen_card
        except IndexError:
            print("Ya no hay mas cartas en la baraja.")
