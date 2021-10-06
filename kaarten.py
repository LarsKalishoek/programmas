import random
soort = ["harten", "klaveren", "schoppen", "ruiten"]
kaartSoort = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "V", "K", "A"]

#generating kaarten deck
def deck():
    kaart = []
    for color in range(0,4):
        selectColor = soort[color]
        for number in range(0,13):
            selectKaartSoort = kaartSoort[number]
            kaart.append(selectColor + " " + selectKaartSoort)
    for a in range(0,2):
        kaart.append("Joker")
    return kaart

def eerste7(cardlist): 
    for y in range(0,7  ):
        pos = y + 1
        print("Kaart " + str(pos) + ": " + cardlist[y])
cards = deck()
random.shuffle(cards)
eerste7(cards)
print("")
print("Deck (47 kaarten) " + str(cards[7:55]))