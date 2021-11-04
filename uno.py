import random

#the list with cards
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
colors = ['blue', 'green', 'red', 'yellow']
special = ['+2', 'skip a turn', 'reverse']
colorless = ["+4", "choose a color"]
deck = []
playerCards = []
aiCards = []
pile = []




#generates the deck of cards
for x in range(4):
    color = colors[x]
    deck.append(color + " 0")
    for z in range(2): 
        for y in range(9):
            deck.append(color +" "+ cards[y])
        for c in range(3):
            deck.append(color + " " + special[c])
for x in range(4):
    for y in range(2):
        deck.append(colorless[y])
random.shuffle(deck)

def startGame():
    input("Press ENTER to start UNO")
    startTurn = random.randint(0, 1)
    for x in range(7):
        aiCards.append(deck[0])
        deck.pop(0)
        playerCards.append(deck[0])
        deck.pop(0)
    pile.append(deck[0])
    deck.pop(0)
    if startTurn == 0:
        print("Player begins.")
    if startTurn == 1:
        print("Opponent begins.")


def showDevinfo():
    # print("the list of cards currently playable: "+ ", ".join(thelist))
    print("the pile in the middle of the table: "+ ", ".join(pile))
    print("your current hand: "+ ", ".join(playerCards))
    print("the enemy's current hand: " + ", ".join(aiCards))

startGame()
showDevinfo()



