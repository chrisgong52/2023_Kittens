from Deck import Deck
from Player import Player

'''

    BE WARY OF PLAYERS PARAMETER BEIGN PASSED BY VALUE;
    NOT SURE IF IT WILL ACTUALLY MODIFY THE ARRAY OBJECTS
    OR IF I IT WILL MODIFY THE COPY

'''

global k_current_player

'''
    attack will take in which player is targetted and have them draw two cards
'''
def attack(players: list, current_player: int, target: int, deck: Deck, discard: Deck):
    players[target].draw(deck)
    players[target].draw(deck)

'''
    see the future will take in who played the card and let them draw three cards
    then prompt them to put them back when done looking
'''
def see_the_future(players: list, current_player: int, target: int, deck: Deck, discard: Deck):
    players[current_player].draw()
    players[current_player].draw()
    players[current_player].draw()
    ''' replace this with frontend prompt '''
    input("press enter when ready to put cards back")
    players[current_player].see_the_future_return(deck)

'''
    shuffle shuffles the deck
'''
def shuffle(players: list, current_player: int, target: int, deck: Deck, discard: Deck):
    deck.shuffle()

'''
    will need to change for multiple input sources

    favor will have a player choose which card to give to the other
    player
'''
def favor(players: list, current_player: int, target: int, deck: Deck, discard: Deck):
    card_to_remove = int(input("choose a card to give up"))
    temp = players[target].remove_card(card_to_remove)
    players[current_player].add(temp)

'''
    will need to change for multiple input sources

    two_kind will allow a player to see the other person's hand and
    choose a card
'''
def two_kind(players: list, current_player: int, target: int, deck: Deck, discard: Deck):
    card_to_remove = int(input("choose a card to take"))
    temp = players[target].remove_card(card_to_remove)
    players[current_player].add(temp)

'''
    CHECK WITH WHAT THE FUNCTIONALITY IS BASED ON RULES

    will need to change for multiple input sources

    three_kind will allow a player to see the other person's hand and
    choose a card
'''
def three_kind(players: list, current_player: int, target: int, deck: Deck, discard: Deck):
    card_to_remove = int(input("choose a card to take"))
    temp = players[target].remove_card(card_to_remove)
    players[current_player].add(temp)


'''
    CHECK WITH WHAT THE FUNCTIONALITY IS BASED ON RULES

    will need to change for multiple input sources

    five_unique will allow a player to see the other person's hand and
    choose a card
'''
def five_unique(players: list, current_player: int, target: int, deck: Deck, discard: Deck):
    card_to_remove = int(input("choose a card to take"))
    temp = players[target].remove_card(card_to_remove)
    players[current_player].add(temp)


'''
    skips one player; only adds one to k_current_player
    because the main will autoincrement and skip will
    not allow players to play until next increment
'''
def skip(players: list, current_player: int, target: int, deck: Deck, discard: Deck):
    global k_current_player
    k_current_player = k_current_player + 1 if k_current_player < len(players)-1 else 0


func_table = {
    "attack": attack,
    "see_the_future": see_the_future,
    "shuffle": shuffle,
    "favor": favor,
    "two_kind": two_kind,
    "three_kind": three_kind,
    "five_unique": five_unique,
    "skip": skip,
}