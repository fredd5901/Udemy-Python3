'''
Text based single deck blackjack game
One player vs an automated dealer
For 1 player, shuffle deck after 5 hands
Blackjack pays 3:2
Win pays 1:1
Dealer is dealt two cards, one face up and one face down
Player is dealt two cards face up
Dealer hits on 16 or less and soft 17; stands on hard 17 or greater
Ties go to the dealer
Player can stand or hit
All players have their turn before the dealer, unless dealer has blackjack
Player can pick their betting amount
Keep track of players total money
Alert the player of wins, losses, busts, etc.
'''

class Card:
    ''' 
    This class represents one playing card for blackjack
    The suit should be a string = 'spade','club','heart', or 'diamond
    The rank should be an integer value of 2 thru 10 or a srting value of 'ace','king','queen' or 'jack'
    Face cards are aasinged a value of 10; aces = 11 and other cards their number value
    If face = 'up' the card is dealt face up; if 'down' then card will be dealt face down
    '''
    
    def __init__(self,suit,rank,face = 'up'): 
        self.suit = suit
        self.rank = rank
        self.face = face
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

class Player():
    '''
    Represents the player in a blackjack game.
    Keeps track of how much cash the player has and how much has bet and won.
    '''
    def __init__(self, cash = 1000): # Player starts with
        self.cash = cash
        self.bet_amt = 0
    def show_cash(self):
        print (self.cash)
    def bet(self):
        betting = True
        while betting:
            print (f'You have ${self.cash}')
            self.bet_amt = int(input('how much do you want to bet?: '))
            if self.bet_amt <= self.cash:
                self.cash = self.cash - self.bet_amt
                print (f'You bet ${self.bet_amt}')
                print (f'You have ${self.cash} left')
                return self.bet_amt  
            else:
                print("you dont' have enough money")
                continue


class Hand():
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.point_total1 = 0
        self.point_total2 = 0
    def add_card(self, card):
        self.cards.append(card)
    def show_hand(self):
        print(f'{self.name} hand is: ')
        for num in range(len(self.cards)):
            if self.cards[num].face == 'up':
                print(self.cards[num].rank, self.cards[num].suit,self.cards[num].face)
            else:
                print('Face Down')
    def num_cards(self):
        return len(self.cards)
    def point_totals(self):
        self.point_total1 = 0
        self.point_total2 = 0
        for num in range(len(self.cards)):
            self.point_total1 = self.point_total1 + self.cards[num].val1
            self.point_total2 = self.point_total2 + self.cards[num].val2
        print (f'Point total: {self.point_total1} or {self.point_total2}')
    
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



def check_hand(hand): # check a hand for a 21 or a bust
    if hand.point_total1 == 21 or hand.point_total2 == 21:
        return '21'
    elif   hand.point_total1 > 21 and hand.point_total2 > 21:
        return 'bust'


# set up the game
player1 = Player()
deck1 = Deck(newdeck()) # get a new unshuffled deck
deck1.shuffle_cards() # shuffle the deck
player1_hand = Hand('player1')
dealer_hand = Hand('dealer')
# start the hand
game_playing = True
print ('\n' * 20)
while game_playing:
    player1_hand.cards = []
    dealer_hand.cards = []
    player1.bet_amt = 0
    print ('\n' * 20)
    # ask the player for their bet
    player1.bet()
    

    # first card to player1
    input('press enter to continue')
    player1_hand.add_card(deck1.deal_card())
    print ('\n' * 100)
    print ('First card dealt to player1:')
    player1_hand.show_hand()
    player1_hand.point_totals()

    # first card to dealer
    input('press enter to continue')
    dealer_hand.add_card(deck1.deal_card())
    dealer_hand.cards[0].face = 'down' # deal first card to dealer face down
    print ('\n' * 100)
    print ('First card dealt to dealer')
    dealer_hand.show_hand()
    dealer_hand.point_totals()
    
    #second cards to player1
    input('press enter to continue')
    player1_hand.add_card(deck1.deal_card())
    print ('\n' * 100)
    print ('Second card dealt to player1: ')
    player1_hand.show_hand()
    player1_hand.point_totals()

    # second card to dealer
    input('press enter to continue')
    print ('\n' * 100)
    dealer_hand.add_card(deck1.deal_card())
    print ('Second card dealt to dealer: ')
    dealer_hand.show_hand()
    dealer_hand.point_totals()

    # show all hands
    input('press enter to continue')
    print ('\n' * 100)
    dealer_hand.show_hand()
    print('')
    player1_hand.show_hand()
    print('')

    # check to see if the dealer or the player has a blackjack
    if check_hand(dealer_hand) == '21':
        print ('Dealer has blackjack. You lose')
        print(f'you lost {player1.bet_amt}')
        print(f'You have ${player1.cash}')
    elif check_hand(player1_hand) == '21':
        print ('Player1 has blackjack. Player1 wins hand')
        print(f'you won {2 * player1.bet_amt}')
        player1.cash = player1.cash + (player1.bet_amt + 2 * player1.bet_amt) #blackjack pays double
        print(f'You have ${player1.cash}')

    else:
        player1_turn = True
        while player1_turn:
            action = input('Do you want to hit or stand? (H or S)')
            if action.lower() == 's':
                player1_turn = False
                dealer_turn = True
            elif action.lower() == 'h':
                print ('\n'*100)
                player1_hand.add_card(deck1.deal_card())
                dealer_hand.show_hand()
                print('')
                player1_hand.show_hand()
                player1_hand.point_totals()
                print('')
                if check_hand(player1_hand) == '21':
                    print ('player1 wins')
                    print(f'you won {player1.bet_amt}')
                    player1.cash = player1.cash + 2 * player1.bet_amt 
                    print(f'You have ${player1.cash}')
                    player1_turn = False
                    dealer_turn = False
                elif check_hand(player1_hand) == 'bust':
                    print ('player1 busted')
                    print(f'you lost {player1.bet_amt}')
                    print(f'You have ${player1.cash}')
                    player1_turn = False
                    dealer_turn = False
                else:
                    continue
        while dealer_turn:
            print('dealer turn')
            dealer_hand.cards[0].face = 'up' # turn over the dealer hole card
            dealer_hand.show_hand()
            dealer_hitting = True
            while dealer_hitting:
                if dealer_hand.point_total1 < 17:
                    print ('dealer hits ')
                    dealer_hand.add_card(deck1.deal_card())
                    dealer_hand.show_hand()
                    dealer_hand.point_totals()
                elif dealer_hand.point_total1 < 17 and dealer_hand.point_total2 == 17: #soft 17
                    print ('dealer hits on soft 17')
                    dealer_hand.cardsadd_card(deck1.deal_card())
                    dealer_hand.show_hand()
                    dealer_hand.point_totals()
                else:
                    print('Dealer Stands')
                    break
            if check_hand(dealer_hand) == 'bust':
                print ('dealer busted...you win ')
                print(f'you won {player1.bet_amt}')
                player1.cash = player1.cash + 2 * player1.bet_amt 
                print(f'You have ${player1.cash}')
                break
            elif check_hand(dealer_hand) == '21':
                print ('dealer has 21')
                print(f'you lost {player1.bet_amt}')
                print(f'You have ${player1.cash}')
                break
            elif dealer_hand.point_total2 > player1_hand.point_total2:
                print ('dealer wins')
                print(f'you lost {player1.bet_amt}')
                print(f'You have ${player1.cash}')
                break
            elif dealer_hand.point_total2 < player1_hand.point_total2:
                print ('player1 wins')
                print(f'you won {player1.bet_amt}')
                player1.cash = player1.cash + 2 * player1.bet_amt 
                print(f'You have ${player1.cash}')
                break
            else:
                print ('PUSH nobody wins')
                print(f'you get your ${player1.bet_amt} bet back')
                player1.cash = player1.cash + player1.bet_amt 
                print(f'You have ${player1.cash}')
                break

    question = input('Play another hand? Y or N:  ')
    if question.lower() == 'y':
        continue
    else:
        break 
    
    















    

