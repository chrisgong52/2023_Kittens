import sys
sys.path.insert(0, '/Users/chrisgong/Desktop/Personal_Projects/2023_Kittens')

from Player import Player
from Deck import Deck


# play special card
def test1():
    p1 = Player("chris", ["tacocat", "attack", "tacocat", "tacocat"])
    temp = p1.play([1])
    return temp[0] == "attack"

# play invalid index
def test2():
    p1 = Player("chris", ["tacocat", "attack", "tacocat", "tacocat"])
    temp = p1.play([-1])
    return temp == False

# play 2 of a kind
def test3():
    p1 = Player("chris", ["tacocat", "attack", "tacocat", "tacocat"])
    temp = p1.play([0,2])
    return temp == ["tacocat", "tacocat"]

# play 3 of a kind
def test4():
    p1 = Player("chris", ["tacocat", "attack", "tacocat", "tacocat"])
    temp = p1.play([0,2,3])
    return temp == ["tacocat", "tacocat", "tacocat"]

# play 5 of a kind
def test5():
    p1 = Player("chris", ["tacocat", "attack", "cattermelon", "skip", "nope"])
    temp = p1.play([0,1,2,3,4])
    return temp == ["nope", "skip", "cattermelon", "attack", "tacocat"]

# play 5 of a kind fail
def test6():
    p1 = Player("chris", ["tacocat", "attack", "skip", "skip", "nope"])
    temp = p1.play([0,1,2,3,4])
    return temp == False

# player draws card
def test7():
    p1 = Player("chris", ["tacocat", "attack", "skip", "skip", "nope"])
    deck = Deck(1, False)
    p1.draw(deck)
    return p1.hand == ["tacocat", "attack", "skip", "skip", "nope", "diffuse"]

func_list = [test1(), test2(), test3(), test4(), test5(), test6(), test7()]


def main():
    count = 1
    for item in func_list:
        if item:
            print("Test", count, "pass")
        else:
            print("Test", count, "failed")
        count = count + 1

main()