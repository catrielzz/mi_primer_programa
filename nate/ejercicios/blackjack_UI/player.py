

class Player:
    def __init__(self):
        self._initial_card = None

    def get_player_card(self):
        return self._initial_card

    def set_player_card(self, initial_card):
        self._initial_card = initial_card
