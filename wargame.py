
import random 

suits=('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
              'Queen':12, 'King':13, 'Ace':14}


'''
card class (suit , rank and values)
'''
 
class Card:
    
    def __init__(self,suit,rank):
        self.suit =suit 
        self.rank =rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
    

'''
 deck class

'''
class Deck:
    
    def __init__(self):

        self.allcards= []

        for suit in suits :
            for rank in ranks:
                created_card= Card(suit,rank)

                self.allcards.append(created_card)
    
    def __str__(self):

        return self.rank +"of" + self.suit


    def shuffle(self):

        random.shuffle(self.allcards)
    
    def deal(self):
        return self.allcards.pop()

'''
 player class(adding, removing and telling how many cards it has) 


'''
class Player(Card):

    def __init__(self,name):
 
        self.name =name
        self.allcards= []


    def __str__(self):
        return (f'{self.name} has {len(self.allcards)} cards ')


    def add_card(self,new_cards):
       
        if type(new_cards) == type([]):
            # for multiple card objects	
            self.allcards.extend(new_cards)
        else:
            # for single card object
            self.allcards.append(new_cards)

    
    def remove_card(self):
        return self.allcards.pop(0)
 
 
 '''
game logic

'''
playerone = Player("one")

playertwo = Player("two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    playerone.add_card(new_deck.deal())
    playertwo.add_card(new_deck.deal())

gameon = True
round=0

while gameon:

    round +=1
    print(f'round {round}')

    if len(playerone.allcards)==0:
        print("Player 2 Wins ")
        gameon = False
        break

    if len(playertwo.allcards)==0:
        print("Player 1 Wins ")
        gameon = False
        break
   #start new round 
    playerone_cards = []
    playerone_cards.append(playerone.remove_card())
    
    playertwo_cards=[]
    playertwo_cards.append(playertwo.remove_card())
    
    # while at war
    atwar = True
    while atwar:

        if playerone_cards[-1].value > playertwo_cards[-1].value :
            playerone.add_card(playertwo_cards)
            playerone.add_card(playertwo_cards)
            atwar=False

        elif playerone_cards[-1].value < playertwo_cards[-1].value :
            playertwo.add_card(playerone_cards)
            playertwo.add_card(playerone_cards)
            atwar=False
    
        else:

            print("At War")

            if len(playerone.allcards)<5:
                print("player 1 dont have enough cards to go for the war!")
                print("player 2 Wins")
                gameon= False
                break

            if len(playertwo.allcards)<5:
                print("player 2 dont have enough cards to go for the war!")
                print("player 1 Wins")
                gameon= False
                break


            else:
                for num in range(5):
                    playerone_cards.append(playerone.remove_card())
                    playertwo_cards.append(playertwo.remove_card())
 
