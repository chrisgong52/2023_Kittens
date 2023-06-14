class Player:
    def __init__(self, name: str, hand = []):
        self.name = name
        self.hand = hand

    def draw(self, deck):
        self.hand.append(deck.draw())