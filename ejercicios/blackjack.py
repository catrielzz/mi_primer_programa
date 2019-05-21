


class Card:
    def __init__(self, number, suit, value):
        self.number - number
        self.suit = suit


class Deck:
    suits = ["diamonds", "heart", "spades", "clubs"]
    max_number = 13

    def __init__(self):
        self.cards = []

        for suit in self.suit:
            for number in range(1, self.max_number + 1):
                self.cards.append(Card(number, suit))

    def give_random_card(self):
        pos = range(0, len(self.cards))

        try:
            return self.cards.pop(pos)
        except IndexError:
            print("Ya no hay mas cartas en la baraja.")


class Game:
    def __init__(self, deck, player):
        self.deck = deck
        self.players = player

    def start_shift(self):
        option = input("Que quieres hacer? [1-Pasar / 2- Pedir]")
        pass

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def main():
    pass


if __name__ == '__main__':
    main()


