class Card:
    ''' 
    This class represents one playing card for blackjack
    The suit should be a string = 'spade','club','heart', or 'diamond
    The rank should be an integer value of 2 thru 10 or a srting value of 'ace','king','queen' or 'jack'
    Face cards are aasinged a value of 10; aces = 11 and other cards their number value
    If face = 'up' the card is dealt face up; if 'down' then card will be dealt face down
    '''
    
    def __init__(self,suit,rank): 
        self.suit = suit
        self.rank = rank
        self.val1 = 0
        self.val2 = 0
        
        if self.rank == 'ace':
            self.val1 = 1
            self.val2 = 11
        elif self.rank == 'king' or self.rank == 'queen' or self.rank == 'jack':
            self.val1 = 10
            self.val2 = 10
        else:
            self.val1 = self.rank
            self.val2 = self.rank
    def __str__(self):
        return self.rank + ' of ' + str(self.suit)
       

class Deck:
    '''
    This class represents a deck of Card objects
    The class constructor takes a list of Card objects
    '''
    
    def __init__(self,cards):
        self.cards = cards # cards is an array of Card ojjects
    def show_deck(self):
        for num in range(len(self.cards)):
            print (f'{self.cards[num].rank} of {self.cards[num].suit} value= {self.cards[num].val1}, {self.cards[num].val2}')
    def num_cards(self): # returns the number of cards in the deck
        return len(self.cards)
    def deal_card(self): # deals out one card that is returned as a Card object
        return self.cards.pop()
    def shuffle_cards(self):
        import random
        random.shuffle(self.cards)
    

class Hand():
    def __init__(self):
        self.cards = []
    
    point_total1 = 0
    point_total2 = 0
    def add_card(self, card):
        self.cards.append(card)
    def show_hand(self):
        for num in range(len(self.cards)):
            print(self.cards[num].rank, self.cards[num].suit)
    def num_cards(self):
        return len(self.cards)
    def point_totals(self):
        for num in range(len(self.cards)):
            self.point_total1 = self.point_total1 + self.cards[num.val1]
            self.point_total2 = self.point_total2 + self.cards[num.val2]
    

def newdeck():
    '''
    This function creates a new deck of 52 cards
    The function returns a list of 52 Card objects sorted in new deck order with all suits together and ranks in order for 2 thru ace
    '''
    cards = []
    suits = ['spade', 'club', 'heart', 'diamond']
    ranks = [2,3,4,5,6,7,8,9,10,'jack','queen','king','ace']

    for suit in suits:
        for rank in ranks:
            cards.append(Card(suit, rank))
    return cards

deck1 = Deck(newdeck())
deck1.show_deck()
print ('')

hand1 = Hand()
hand2 = Hand()
hand3 = Hand()

card1 = deck1.deal_card()
print ('card1:')
print (card1)
print ('')

card2 = deck1.deal_card()
print ('card2:')
print (card2)
print ('')

card3 = deck1.deal_card()
print ('card3:')
print (card3)
print ('')

card4 = deck1.deal_card()
print ('card4:')
print (card3)
print ('')

print ('hand1:')
hand1.add_card(card1)
hand1.show_hand()
print ('')

print ('hand2:')
hand2.add_card(card2)
hand2.show_hand()
print ('')

print ('hand3:')
hand3.add_card(card3)
hand3.show_hand()
print ('')







    