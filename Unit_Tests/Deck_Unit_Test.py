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

# shuffle
def test3():
    deck = Deck(1, False)
    temp = []
    for item in deck.deck:
        temp.append(item)
    deck.shuffle()
    temp2 = deck.deck
    return temp != temp2

# insert diffuse
def test4():
    deck = Deck(2, False)
    deck.insert_diffuse()
    count = 0
    for item in deck.deck:
        if item == "diffuse":
            count = count + 1
    return count == 4

# insert kittens
def test5():
    deck = Deck(2, False)
    deck.insert_kittens()
    count = 0
    for item in deck.deck:
        if item == "exploding_kitten":
            count = count + 1
    return count == 1

func_list = [test1(), test2(), test3(), test4(), test5()]

def main():
    count = 1
    for item in func_list:
        if item:
            print("Test", count, "pass")
        else:
            print("Test", count, "failed")
        count = count + 1

main()