from PIL import Image, ImageTk


class Card:
    number_name_mapping = {
        1: "ace",
        11: "jack",
        12: "queen",
        13: "king"
    }

    card_image_path = "./assets/png/"

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.tk_img = ImageTk.PhotoImage(
            Image.open(
                f"{self.card_image_path}{self.number_name_mapping.get(self.number, self.number)}_of_{self.suit}.png"))
