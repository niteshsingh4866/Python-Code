import random
import os
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
cards={}
def createCard():
    for s in suits:
        cards[s]=ranks.copy()
    print('\n cards ready to be distributed')
createCard()
handsNum=0
playerRemaningCredit=0
currentCredit=0
computerCredit=0
playerCard=[]
computerCard=[]
#print(cards)
class UpdateCards():
    def __init__(self,r,s):
        cards[s].remove(r)     

class Credit():
    def __init__(self):
        global currentCredit
        if handsNum == 0:
            currentCredit=0
            while True:
                currentCredit=int(input('Enter the current Betting Amount: '))
                if (playerRemaningCredit-currentCredit) < 0:
                    print('Enter the amount from remaining credit')
                else:
                    break
        else:
            bet=input('Do you want to raise the Bet press y/n: ')
            if bet == 'y':
                while True:
                    amount=int(input('Enter the amount if you want to raise the bet: '))
                    if (playerRemaningCredit-(currentCredit+amount)) < 0:
                        print('Enter the amount from the remaning credit')
                    else:
                        currentCredit=currentCredit+amount
                        break
class DisplayHands():
    def __init__(self):
        #os.system('cls')
        print('\nDealers Card\n-------------')
        for i in computerCard:
            if handsNum == 0 and computerCard[0] == i: 
                print('<card is hidden>')
            else:
                print(i)
        print('\nPlayers Card\n-------------')
        for i in playerCard:
            print(i)

class winORbust():
    playerScore=0
    computerScore=0
    result=0
    aceCount=0
    def __init__(self):
        global playerRemaningCredit
        for x in playerCard:
            if x.split(' ')[0] == 'Ace':
                self.aceCount+=1
                if self.aceCount > 1:
                   self.playerScore=self.playerScore+1
                else:
                    self.playerScore=self.playerScore+values[x.split(' ')[0]]
            else:         
                self.playerScore=self.playerScore+values[x.split(' ')[0]]
        self.aceCount=0
        for y in computerCard:
            if y.split(' ')[0] == 'Ace':
                self.aceCount+=1
                if self.aceCount > 1:
                   self.computerScore=self.computerScore+1
                else:
                    self.computerScore=self.computerScore+values[y.split(' ')[0]]
            else:         
                self.computerScore=self.computerScore+values[y.split(' ')[0]]
        d=DisplayHands()
        #print('player score = ',self.playerScore)
        #print('computer score = ',self.computerScore)
        if self.playerScore == 21 or self.computerScore>21:
            print('Congratulations you won')
            playerRemaningCredit+=currentCredit
            print('playerRemaningCredit: ',playerRemaningCredit)
            self.result=1
        if self.computerScore == 21 or self.playerScore >21:
            print('Sorry you lost')
            playerRemaningCredit-=currentCredit
            print('playerRemaningCredit: ',playerRemaningCredit)
            self.result=1 

print('welcome to the Game')
playerRemaningCredit=int(input('Enter the total Credit amount for the table: '))
while True:
    yn=input('\npress y to start the game else press n to end the game: ')
    if yn =='y' and handsNum==0:
        c=Credit()
        for i in range(0,4):
            if i%2==0:
                s=random.choice(suits)
                r=random.choice(cards[s])
                tempstr=r+' of '+s
                playerCard.append(tempstr)
                u=UpdateCards(r,s)
            else:
                s=random.choice(suits)
                r=random.choice(cards[s])
                tempstr=r+' of '+s
                computerCard.append(tempstr)
                u=UpdateCards(r,s)
        w=winORbust().result
        handsNum=handsNum+1
        if w == 1:
            cards={}
            createCard()
            handsNum=0
            playerCard=[]
            computerCard=[]
            #break
        #handsNum=handsNum+1
        if(yn =='y' and handsNum>0):
            c=Credit()
            while True:
                sh=input('Do you want to stand(press s) or hit(press h): ')
                if sh == 's':
                    s=random.choice(suits)
                    r=random.choice(cards[s])
                    tempstr=r+' of '+s
                    computerCard.append(tempstr)
                    u=UpdateCards(r,s)
                    w=winORbust().result
                    if w == 1:
                        cards={}
                        createCard()
                        handsNum=0
                        playerCard=[]
                        computerCard=[]
                        break  
                if sh == 'h':
                    s=random.choice(suits)
                    r=random.choice(cards[s])
                    tempstr=r+' of '+s
                    playerCard.append(tempstr)
                    u=UpdateCards(r,s)
                    w=winORbust().result
                    if w == 1:
                        cards={}
                        createCard()
                        handsNum=0
                        playerCard=[]
                        computerCard=[]
                        break    
                    s=random.choice(suits)
                    r=random.choice(cards[s])
                    tempstr=r+' of '+s
                    computerCard.append(tempstr)
                    u=UpdateCards(r,s)
                    w=winORbust().result
                    if w == 1:
                        cards={}
                        createCard()
                        handsNum=0
                        playerCard=[]
                        computerCard=[]
                        break
    if playerRemaningCredit == 0:
        print('Sorry you lost everything.Come again Tomorrow')
        break
    if yn=='n':
        print('Bye')
        break                  

    