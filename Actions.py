'''
    Actions will be the intermediary between the decks and players
'''

from Deck import Deck
from Player import Player

class Action:
    '''
        params: list of players in the game
        init will initialize the players array and create a deck and discard pile
    '''
    def __init__(self, players: list):
        self.players = players
        self.func_table = {
            "attack": self.attack,
            "see_the_future": self.see_the_future,
            "shuffle": self.shuffle,
            "favor": self.favor,
            "two_kind": self.two_kind,
        }

    '''
        attack will take in which player is targetted and have them draw two cards
    '''
    def attack(self, current_player: int, target: int, deck: Deck):
        self.players[target].draw(self.deck)
        self.players[target].draw(self.deck)

    '''
        see the future will take in who played the card and let them draw three cards
        then prompt them to put them back when done looking
    '''
    def see_the_future(self, current_player: int, target: int, deck: Deck):
        self.players[current_player].draw()
        self.players[current_player].draw()
        self.players[current_player].draw()
        ''' replace this with frontend prompt '''
        input("press enter when ready to put cards back")
        self.players[current_player].see_the_future_return(self.deck)

    '''
        shuffle shuffles the deck
    '''
    def shuffle(self, current_player: int, target: int, deck: Deck):
        deck.shuffle()

    '''
        will need to change for multiple input sources

        favor will have a player choose which card to give to the other
        player
    '''
    def favor(self, current_player: int, target: int, deck: Deck):
        card_to_remove = int(input("choose a card to give up"))
        temp = self.players[target].remove_card(card_to_remove)
        self.players[current_player].add(temp)

    '''
        will need to change for multiple input sources

        two_kind will allow a player to see the other person's hand and
        choose a card
    '''
    def two_kind(self, current_player: int, target: int, deck: Deck):
        card_to_remove = int(input("choose a card to take"))
        temp = self.players[target].remove_card(card_to_remove)
        self.players[current_player].add(temp)