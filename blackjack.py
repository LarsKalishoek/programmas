import random
import os
import time

colors = ["Heart", "Clover", "Spade", "Diamond"]
numbers = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = []
player = []
dealer = []
multi = 1
bet = 0
tokens = 1000

#generating kaarten deck

for x in range(0, 4):
    for y in range(0, 13):
        deck.append(colors[x] + " " + numbers[y])

def newDeck():
    deck.extend(pile)
    random.shuffle(deck)

def buy(x):
    x.append(deck[0])
    deck.pop(0)
    
def options():
    global multi
    opt = "B) Buy    S)Stop    D)Double down"
    score = calcCards(player)
    if calcCards(player) > 21:
        print("You've gone bust".center(50))
        time.sleep(1.5)
        dealerRound()
    elif score == 21 and len(player) == 2:
        multi = 1.5
    print(opt.center(51))
    ans = input("").lower()
    if ans == "b":
        buy(player)
        refresh()
        options()
    elif ans == "s":
        dealerRound()
    elif ans == "d":
        buy(player)
        multi = 2
        dealerRound()
    else:
        refresh()
        options()
        
def refresh(turn="hi", winner = "none"):
    clear()
    board(turn, winner)

 
random.shuffle(deck)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcCards(cards):
    total = 0
    ace = 0
    special =["J", "Q", "K"]
    for x in cards:
        for y in range(2,11):
            if str(y) in x:
                total += y
        for q in special:
            if q in x:
                total += 10 
        if "A" in x:
            total += 11
            ace += 1
    for x in range(1,5):
        if total > 21 and ace >= x:
            total -= 10
        else:
            break
    return total

def firstDeal(cards):
    total = 0
    special =["J", "Q", "K"]
    for x in cards:
        for y in range(2,11):
            if str(y) in x:
                total += y
                return total
        for q in special:
            if q in x:
                total += 10 
                return total
        if "A" in x:
            total += 11
            return total
            

def giveCards():
    for x in range(2):
        player.append(deck[0])
        deck.pop(0)
        dealer.append(deck[0])
        deck.pop(0)

def empty():
    for x in range(len(player)):
        deck.append(player[0])
        player.pop(0)
    for x in range(len(dealer)):
        deck.append(dealer[0])
        dealer.pop(0)
    random.shuffle(deck)



def winner():
    scorePlayer = calcCards(player) 
    scoreDealer = calcCards(dealer)
    if scorePlayer <= 21 and scorePlayer > scoreDealer or scorePlayer <= 21 and scoreDealer > 21:
        return "player"
    elif scorePlayer == scoreDealer:
        return "tie"
    else:
        return "dealer"

def endround():
    win = winner()
    refresh("dealer", win)
    ans = input("Do you want to play another round?  Y/N  : ").lower()
    if ans == "y":
        empty()
        gameRound()
    if ans == "n":
        clear()
        print("You ended with", tokens, "tokens.")
        input("Press enter to exit game")
        exit()


def board(turn, winner):
    global tokens
    multiplier = int(multi*bet)
    D = "Dealer:"
    if turn == "dealer":
        dealerHand = ', '.join(map(str, dealer))
        dealerScore = calcCards(dealer)
    else:
        dealerHand = dealer[0]+", Hidden"
        dealerScore = firstDeal(dealer)
    score = calcCards(player)
    if score == 21 and len(player) == 2:
        playerScore = "Blackjack"
    else:
        playerScore = score
    P = "Player:"
    playerHand = ', '.join(map(str, player))
    print(str(dealerScore).center(50))
    print(D.center(50))
    print(dealerHand.center(50))
    if winner == "none":
        print("")
    elif winner == "tie":
        print("You tied you lost noting".center(50))
        tokens += bet
    elif winner == "player":
        text = ("You won and got "+ str(multiplier*2) +" tokens")
        print(text.center(50))
        tokens += (multiplier*2)
    elif winner == "dealer":
        text = ("You lost and lost "+ str(multiplier) +" tokens")
        tokens -= multiplier-bet
        print(text.center(50))
    print(str(playerScore).center(50))
    print(P.center(50))
    print(playerHand.center(50))




def dealerRound():
    score = calcCards(dealer)
    refresh("dealer")
    time.sleep(1)
    if calcCards(player) > 21:
        endround()
    if score < 17:
        buy(dealer)
        dealerRound()
    elif score > 21:
        print("Dealer has gone bust".center(50))
        endround()
    else:
        endround()


def gameRound():
    global multi, bet, tokens
    multi = 1
    clear()
    print("Your tokens", tokens)
    bet = input("How many tokens do you want to bet?  : ")
    if bet.isdigit() == False:
        gameRound()
    if int(bet) != float(bet):
        gameRound()
    tokens -= int(bet)
    bet = int(bet)
    giveCards()
    refresh()
    options()


def startGame():
    input("Press ENTER to start")
    gameRound()

 
startGame()
