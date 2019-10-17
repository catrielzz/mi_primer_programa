"""
player-
dealer-
card_values-
deck-
table_cards
draft_card()
calculate_score()
give_initial_cards()
"""
from nate.ejercicios.blackjack_UI.deck import Deck
from nate.ejercicios.blackjack_UI.player import Player


class BlackJack:
    card_values = {
        1: 11,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 10,
        12: 10,
        13: 10
    }

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()
        self.table_cards = []

    def give_initial_cards(self):
        player_card = self.deck.give_random_card()
        dealer_card = self.deck.give_random_card()
        self.player.set_player_card(player_card)
        self.dealer.set_player_card(dealer_card)
        return player_card, dealer_card

    def draft_card(self):
        card = self.deck.give_random_card()
        self.table_cards.append(card)
        return card

    def _calculate_score(self, player_card):
        total = 0
        cards = [player_card]
        cards.extend(self.table_cards)

        for card in cards:
            if card.number == 1 and total + self.card_values[card.number] > 21:
                total += 1
            else:
                total += self.card_values[card.number]
        return total

    def get_table_cards_count(self):
        return len(self.table_cards)

