from tkinter import ttk
from tkinter import *

from nate.ejercicios.blackjack_UI.black_jack import BlackJack


class BlackJackUI:
    def __init__(self):
        self.game = None
        self.ui_player_card_label = None

        self.ui_root = Tk()
        # Title Frame
        self.ui_title_frame = ttk.Frame(self.ui_root, padding="30 12 30 12")
        self.ui_title_frame.grid(sticky=(W, E))
        # Table Frame
        self.ui_table_frame = ttk.Frame(self.ui_root, padding="30 12 30 12", width=200, height=450)
        self.ui_table_frame.grid(sticky=(W, E))
        # Score Frame
        self.ui_score_frame = ttk.Frame(self.ui_root, padding="30 12 30 12")
        self.ui_score_frame.grid(sticky=(W, E))
        # Row Configure
        self.ui_table_frame.rowconfigure(1, minsize=150)
        self.ui_table_frame.rowconfigure(2, minsize=150)
        self.ui_score_frame.rowconfigure(3, minsize=150)
        # Labels
        ttk.Label(self.ui_title_frame, text="BlackJack", width=60).grid(column=1, row=1)
        ttk.Label(self.ui_score_frame, text="Tus puntos:").grid(column=1, row=1)
        ttk.Label(self.ui_score_frame, text="Puntos dealer:").grid(column=3, row=1)

        self.ui_player_score_label = ttk.Label(self.ui_score_frame, text="0", width=12)
        self.ui_player_score_label.grid(column=2, row=1)

        self.ui_dealer_score_label = ttk.Label(self.ui_score_frame, text="???", width=12).grid(column=4, row=1)

        # Buttons
        ttk.Button(self.ui_title_frame, text="Jugar", command=self.start_game).grid(column=2, row=1)

        self.ui_end_game_button = ttk.Button(self.ui_score_frame, text="Plantarse",
                                             state=DISABLED, command=self.end_game).grid(column=5, row=1)
        self.ui_another_card_button = ttk.Button(self.ui_score_frame, text="Pedir carta",
                                                 state=DISABLED, command=self.draft_card).grid(column=6, row=1)

    def start_game(self):
        self.game = BlackJack()
        player_card, dealer_card = self.game.give_initial_cards()

        self.ui_player_card_label = ttk.Label(self.ui_table_frame, image=player_card.tk_img).grid(column=1, row=3)
        self.ui_player_card_label = player_card.tk_img
        self.ui_player_card_label.pack()

    def draft_card(self):
        pass

    def end_game(self):
        pass

    def run(self):
        self.ui_root.mainloop()


if __name__ == "__main__":
    BlackJackUI().run()

