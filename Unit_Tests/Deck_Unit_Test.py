import sys
sys.path.insert(0, '/Users/chrisgong/Desktop/Personal_Projects/2023_Kittens')

from Player import Player
from Deck import Deck

# player draws card
def test1():
    p1 = Player("chris", ["tacocat", "attack", "skip", "skip", "nope"])
    deck = Deck(1, False)
    temp = len(deck)
    p1.draw(deck)
    return len(deck) == temp - 1

# player plays a card
def test2():
    p1 = Player("chris", ["tacocat", "attack", "skip", "skip", "nope"])
    deck = Deck(1, True)
    played = p1.play([1])
    for item in played:
        deck.push(item)
    return deck.peek() == "attack" and len(deck) == 1

func_list = [test1(), test2()]

def main():
    count = 1
    for item in func_list:
        if item:
            print("Test", count, "pass")
        else:
            print("Test", count, "failed")
        count = count + 1

main()