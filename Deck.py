import random

class Deck:
    def __init__(self, player_count: int):
        self.player_count = player_count
        self.deck = []
        for item in range(self.player_count):
            self.deck.append("diffuse")
            self.deck.append("exploding_kitten")
        self.deck.pop(-1)
        general_cards = ["tacocat", "cattermelon", "beard_cat", "hairy_potato_cat", "rainbow_cat", "attack", "shuffle", "favor", "skip"]
        additional_cards = ["see_the_future", "nope"]
        for item in general_cards:
            for el in range(4):
                self.deck.append(item)
        for item in additional_cards:
            for el in range(5):
                self.deck.append(item)

        self.shuffle()
        for item in self.deck:
            print(item)

        self.func_table = {
            "shuffle": self.shuffle,
            "draw": self.draw,
        }

    '''
        draw returns the top card from the deck and removes the top card
        the top card is index 0

        return the top card if deck not empty, else false
    '''
    def draw(self):
        if len(self.deck) > 0:
            out = self.deck[0]
            self.deck.pop(0)
            return out
        else:
            return False
    
    '''
        shuffle shuffles the deck
    '''
    def shuffle(self):
        random.shuffle(self.deck)
        return True