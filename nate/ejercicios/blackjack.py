import random

# Class Card

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.number, self.suit)

# Class Deck
class Deck:
    suits = ["diamonds", "heart", "spades", "clubs"]
    max_number = 13

    def __init__(self):
        self.cards = []

        for suit in self.suits:
            for number in range(1, self.max_number + 1):
                self.cards.append(Card(number, suit))

    def give_random_card(self):
        pos = random.randint(0, len(self.cards))

        try:
            return self.cards.pop(pos)
        except IndexError:
            print("Ya no hay mas cartas en la baraja.")

    def __str__(self):
        str_cards = [str(card) for card in self.cards]
        return "Mazo con {} cartas: \n{}".format(len(self.cards), ",\n".join(str_cards))


class Game:
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

    n_players = 2

    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.table_cards = []

    def ask_player_name(self, player_n):
        return input("Cual es el nombre del jugador {}?".format(player_n))

    def draft_card(self):
        card = self.deck.give_random_card()
        self.table_cards.append(card)
        print(card)
        return card

    def count_table_cards(self):
        total = 0
        for card in self.table_cards:
            if card.number == 1 and total + self.card_values[card.number] > 21:
                total += 1
            else:
                total += self.card_values[card.number]
        return total

    def player_wants_to_continue(self):
        response = input("Quieres otra carta? (Y/N)").upper()
        return response == "Y"

    def start_turn(self, player):
        self.table_cards = []
        self.deck = Deck()
        print("Turno del jugador {}\n\n".format(player.name))

    def run(self):
        for i in range(self.n_players):
            self.players.append(Player(self.ask_player_name(i + 1)))

        winner_score = 0
        winner = None

        for player in self.players:
            self.start_turn(player)
            # print("Turno del jugador {}\n\n".format(player.name))

            user_continue = True

            while user_continue and self.count_table_cards() < 21:
                self.draft_card()
                user_continue = self.player_wants_to_continue()

            player.score = self.count_table_cards()
            print("Tu puntuacion es de: {}".format(player.score))

            if player.score > 21:
                print("Has perdido")
            elif player.score > winner_score:
                winner_score = player.score
                winner = player

        print("El ganador es: {}".format(winner.name))


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


def main():
    pass


if __name__ == '__main__':
    blackjack = Game()
    blackjack.run()


