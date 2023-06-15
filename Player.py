class Player:
    def __init__(self, name: str, hand = []):
        self.name = name
        self.hand = hand
        self.specials = set(["see_the_future", "nope", "attack", "shuffle", "favor", "skip", "diffuse", "exploding_kitten"])

    '''
        repr for printing the player if print(player) called 
    '''
    def __repr__(self):
        return str(self.hand)
    
    '''
        print will print the player's hand
    '''
    def print(self):
        print(self.hand)

    '''
        params: deck is the deck to draw from
        draw draws a card from the top of the deck and adds it
        to the player's hand
    '''
    def draw(self, deck):
        self.hand.append(deck.draw())
    
    '''
        params: indices is the indices in the hand for cards to play
        valid_check will return whether the indices played are valid
        based on the cards in the player's hand
    '''
    def valid_check(self, indices):
        # check to make sure the indices are within the length of the hand
        for item in indices:
            if item >= len(self.hand) or item < 0:
                # print("invalid index", item, len(self.hand))
                return False
        
        # check to make sure all indices unique
        unique = set(indices)
        if len(unique) != len(indices):
            # print("not unique indices")
            return False
        
        # check to see if len is 1 if it's a special card
        if len(indices) == 1:
            if self.hand[indices[0]] not in self.specials:
                # print("single non special")
                return False
            
        # check to make sure 2 or 3 of a kind all match
        if len(indices) == 2 or len(indices) == 3:
            temp = self.hand[indices[0]]
            for item in indices:
                if self.hand[item] != temp:
                    # print("2/ 3 of a kind not matching")
                    return False
        
        # check to make sure 5 unique cards are all unique
        if len(indices) == 5:
            played = set([])
            for item in indices:
                played.add(self.hand[item])
            if len(played) != 5:
                # print("5 of a kind not unique")
                return False
            
        return True

    '''
        params: indices is the indices in the hand for cards to play
        play returns the card played from the hand if
        index is valid
        
        return list of cards if played, else false
    '''
    def play(self, indices: list):
        if not self.valid_check(indices):
            return False
        played = []
        indices.sort(reverse = True)
        for item in indices:
            played.append(self.hand[item])
            self.hand.pop(item)
        return played
    
    '''
        see_the_future_play puts the last three cards onto the deck in
        the same order as they were seen
    '''
    def see_the_future_return(self, deck):
        for _ in range(3):
            deck.push(self.hand[-1])
            self.hand.pop(-1)
    
    '''
        params:
            index: card to remove
        remove_card will remove a card from a player's hand
        without checks
    '''
    def remove_card(self, index: int):
        if index < len(self.hand):
            temp = self.hand[index]
            self.hand.pop(index)
            return temp
        else:
            return False
        
    '''
        params:
            card: string of the name of the card to add to player's hand
        add will add a card to the player's hand
    '''
    def add(self, card: str):
        self.hand.append(card)