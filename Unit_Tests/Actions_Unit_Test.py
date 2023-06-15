import sys
sys.path.insert(0, '/Users/chrisgong/Desktop/Personal_Projects/2023_Kittens')

from Player import Player
from Deck import Deck
from Actions import Action

# player draws card
def test1():
    Action(2)
    
    return

func_list = [test1()]

def main():
    count = 1
    for item in func_list:
        if item:
            print("Test", count, "pass")
        else:
            print("Test", count, "failed")
        count = count + 1

main()