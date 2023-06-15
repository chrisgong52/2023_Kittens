import random

class Deck:
    def __init__(self, player_count: int, discard: bool = False, shuffle: bool = True):
        self.deck = []
        if not discard:
            self.player_count = player_count
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

            if shuffle:
                self.shuffle()

            self.func_table = {
                "shuffle": self.shuffle,
                "draw": self.draw,
            }

    '''
        repr is to print out the deck if we call print(deck)
    '''
    def __repr__(self):
        return str(self.deck)
    
    '''
        len will return the length of the deck
    '''
    def __len__(self):
        return len(self.deck)

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
    
    '''
        print is for if we call deck.print()
    '''
    def print(self):
        print(self.deck)

    '''
        params: card is the card that will be put onto the deck
        note: for playing multiple of a kind, push cards on one by one
        push will be how a discard pile will add a card or generally how to put cards
        back onto the deck (see the future)
    '''
    def push(self, card):
        self.deck.insert(0, card)

    '''
        peek returns the top card of the deck without modification
    '''
    def peek(self):
        return self.deck[0]