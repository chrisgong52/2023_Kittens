from Deck import Deck
from Player import Player
from Actions import Action
import Play_Functions

def print_state(deck, discard, players):
    print(deck)
    print(discard)
    for item in players:
        print(item)

def main():
    global k_current_player

    '''
        initialization
    '''
    k_current_player = 0
    player_count = 2
    deck = Deck(player_count)
    discard = Deck(player_count, True)
    players = []
    for _ in range(player_count):
        players.append(Player([]))
    for _ in range(4):
        for cur in range(player_count):
            players[cur].draw(deck)

    deck.insert_diffuse()
    deck.insert_kittens()
    for item in players:
        item.add("diffuse")

    # print_state(deck, discard, players)

    
    # while len(players) > 1:
    #     players[k_current_player].draw(deck)
    #     k_current_player = k_current_player + 1
    


if __name__ == "__main__":
    main()