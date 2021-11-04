import random
diceNumbers = ['1', '2', '3', '4', '5', '6']
stored = []
rollTimes = 0
vari = True
small1 = ["1", "2", "3", "4"]
small2 = ["2", "3", "4", "5"]
small3 = ["3", "4", "5", "6"]
big1   = ["1", "2", "3", "4", "5"]
big2   = ["2", "3", "4", "5", "6"]
roundNum = 0
scoreDic = {
    "aces" : "0",
    "twos" : "0",
    "threes" : "0",
    "fours" : "0",
    "fives" : "0",
    "sixes" : "0",
    "three of a kind" : "0",
    "four of a kind" : "0",
    "full house" : "0",
    "small straight" : "0",
    "large straight" : "0",
    "yahtzee" : "0",
    "chance" : "0",
    "total points" : "0",
    "total points 1" : "0",
    "total points 2" : "0",
    "total" : "0",
    "bonus": "0"
}

def game():
    input("Press ENTER to start game")
    global roundNum
    roundNum += 1

def roll(keptDice:list = []):
    if roundNum > 13:
        scoreboard()
        input()
        exit()
    global rollTimes
    rollTimes += 1
    diceAmount = 5 - len(keptDice)
    rollDice = []
    for x in range(0, diceAmount):
        rollDice.append(random.choice(diceNumbers))
    print("Stored dice: " + str(keptDice))
    print("You rolled: " + str(rollDice))
    if rollTimes < 3:
        keptDices = keepDice(rollDice, keptDice)
    alldice = rollDice + keptDice
    checkScore(alldice)
    if rollTimes < 3:
        choice(keptDices, alldice)
    elif rollTimes == 3:
        kiesPunten(alldice)
        
def choice(keptDice, dice):
    ans = input("Roll or Score?: ").lower()
    if ans == "roll":
        roll(keptDice)
    elif ans == "score":
        kiesPunten(dice)
    elif ans == "board":
        scoreboard()
    
        choice(keptDice, dice)
    else:
        choice(keptDice, dice)

def kiesPunten(dice:list):
    scoreType = input("What catagory do you choose? ").lower()
    if scoreType == "board":
        scoreboard()
        kiesPunten(dice)
    calculateScore(dice, scoreType)
    global roundNum
    roundNum += 1
    global rollTimes
    rollTimes = 0
    roll([])

#choice for keeping dice from roll or putting them back
def keepDice(rollDice:list, keptDice:list):
    while len(keptDice) <= 5:
        rdice = rollDice.copy()
        kdice = keptDice.copy()
        ans1 = input("Keep or Return: ").lower()
        splitAns = ans1.split()
        if splitAns[0] == "stop":
            break
        if splitAns[0] != "keep" and splitAns[0] != "return":
            print("Type stop to exit")
            continue
        splitAns.pop(0)
        sP1 = splitAns.copy()
        sP2 = splitAns.copy()
        if keep(rdice, sP1) == True and "keep" in ans1:
            for y in range(0,len(splitAns)):
                keptDice.append(splitAns[y])
                rollDice.remove(splitAns[y])
        elif returN(kdice, sP2) == True and "return" in ans1:
            for y in range(0,len(splitAns)):
                keptDice.remove(splitAns[y])
                rollDice.append(splitAns[y])
        else:
            print("Type stop to exit")
        print(keptDice)
        print(rollDice)
    return keptDice


def keep(dices, ansKeep):
    if len(ansKeep) > len(dices):
        vari = False
    else:
        for x in range(0, len(ansKeep)):
            vari = all(elem in dices  for elem in ansKeep)
            if vari == False:
                break
            dices.remove(ansKeep[0])
            ansKeep.pop(0)
    return vari

def returN(kepdice, ansKeep):
    if len(ansKeep) > len(kepdice):
        variable = False
    else:
        for x in range(0, len(ansKeep)):
            variable = all(elem in kepdice  for elem in ansKeep)
            if variable == False:
                break
            kepdice.remove(ansKeep[0])
            ansKeep.pop(0)
    return variable

def checkScore(dice:list):
    if "1" in dice and scoreDic.get("aces") == "0":
        var1 = dice.count("1")
        print("aces           : ", var1*1)
    if "2" in dice and scoreDic.get("twos") == "0":
        var2 = dice.count("2")
        print("twos           : ", var2*2)
    if "3" in dice and scoreDic.get("threes") == "0":
        var3 = dice.count("3")
        print("threes         : ", var3*3)
    if "4" in dice and scoreDic.get("fours") == "0":
        var4 = dice.count("4")
        print("fours          : ", var4*4)
    if "5" in dice and scoreDic.get("fives") == "0":
        var5 = dice.count("5")
        print("fives          : ", var5*5)
    if "6" in dice and scoreDic.get("sixes") == "0":
        var6 = dice.count("6")
        print("sixes          : ", var6*6)
    if threeKind(dice, 1) == True and scoreDic.get("three of a kind") == "0":
        print("three of a kind: ", threeKind(dice,0))
    if fourKind(dice, 1) == True and scoreDic.get("four of a kind") == "0":
        print("four  of a kind: ", fourKind(dice,0))
    if fullHouse(dice) == True and scoreDic.get("full house") == "0":
        print("full house     :  25")
    if smallStraight(dice) == True and scoreDic.get("small straight") == "0":
        print("small straight :  30")
    if bigStraight(dice) == True and scoreDic.get("large straight") == "0":
        print("large straight :  40")
    if yahtzee(dice) == True and scoreDic.get("yahtzee") == "0":
        print("yahtzee        :  50")
    if yahtzee(dice) == True and scoreDic.get("yahtzee") != "0" and scoreDic.get("yahtzee") != 0:
        print("extra yahtzee  :  100")
    if scoreDic.get("chance") == "0":
        print("chance         : ", (int(dice[0])+int(dice[1])+int(dice[2])+int(dice[3])+int(dice[4])))

def calculateScore(dice:list, catagory:str):
    global scoreDic
    if scoreDic.get("aces") == "0" and catagory == "aces":
        var1 = dice.count("1")
        scoreDic.update({"aces": var1*1})
    elif scoreDic.get("twos") == "0" and catagory == "twos":
        var2 = dice.count("2")
        scoreDic.update({"twos": var2*2})
    elif scoreDic.get("threes") == "0" and catagory == "threes":
        var3 = dice.count("3")
        scoreDic.update({"threes": var3*3})
    elif scoreDic.get("fours") == "0" and catagory == "fours":
        var4 = dice.count("4")
        scoreDic.update({"fours": var4*4})
    elif scoreDic.get("fives") == "0" and catagory == "fives":
        var5 = dice.count("5")
        scoreDic.update({"fives": var5*5})
    elif scoreDic.get("sixes") == "0" and catagory == "sixes":
        var6 = dice.count("6")
        scoreDic.update({"sixes": var6*6})
    elif scoreDic.get("three of a kind") == "0" and catagory == "three of a kind":
        if threeKind(dice, 1) == False:
            scoreDic.update({"three of a kind": 0})
            return
        scoreDic.update({"three of a kind": threeKind(dice,0)})
    elif scoreDic.get("four of a kind") == "0" and catagory == "four of a kind":
        if fourKind(dice, 1) == False:
            scoreDic.update({"four of a kind": 0})
            return
        scoreDic.update({"four of a kind": fourKind(dice,0)})
    elif scoreDic.get("full house") == "0" and catagory == "full house":
        if fullHouse(dice) == False:
            scoreDic.update({"full house": 0})
            return
        scoreDic.update({"full house": 25})
    elif scoreDic.get("small straight") == "0" and catagory == "small straight":
        if smallStraight(dice) == False:
            scoreDic.update({"small straight": 0})
            return
        scoreDic.update({"small straight": 30})
    elif scoreDic.get("large straight") == "0" and catagory == "large straight":
        if bigStraight(dice) == False:
            scoreDic.update({"large straight": 0})
            return
        scoreDic.update({"large straight": 40})
    elif scoreDic.get("yahtzee") == "0" and catagory == "yahtzee":
        if yahtzee(dice) == False:
            scoreDic.update({"yahtzee": 0})
            return
        scoreDic.update({"yahtzee": 50})
    elif scoreDic.get("yahtzee") != "0" and scoreDic.get("yahtzee") != 0 and catagory == "yahtzee":
        varY = scoreDic.get("yahtzee")
        varY += 100
        scoreDic.update({"yahtzee": varY})
    elif scoreDic.get("chance") == "0" and catagory == "chance":
        scoreDic.update({"chance": (int(dice[0])+int(dice[1])+int(dice[2])+int(dice[3])+int(dice[4]))})
    else:
        kiesPunten(dice)

def threeKind(dice:list, version):
    for z in range(1, 7):
        count_ = dice.count(str(z))
        if count_ == 3 and version == 0:
            return (int(dice[0])+int(dice[1])+int(dice[2])+int(dice[3])+int(dice[4]))
        elif count_ == 3 and version == 1:
            return True
    return False

def fourKind(dice:list, version):
    for z in range(1, 7):
        count_ = dice.count(str(z))
        if count_ == 4 and version == 0:
            return (int(dice[0])+int(dice[1])+int(dice[2])+int(dice[3])+int(dice[4]))
        elif count_ == 4 and version == 1:
            return True
    return False

def fullHouse(dice:list):
    for z in range(1, 7):
        count_ = dice.count(str(z))
        if count_ == 3:
            for z in range(1, 7):
                count_ = dice.count(str(z))
                if count_ == 2:
                    return True
    return False

def smallStraight(dice:list):
    if all(elem in dice for elem in small1) == True:
        return True
    if all(elem in dice for elem in small2) == True:
        return True
    if all(elem in dice for elem in small3) == True:
        return True
    return False

def bigStraight(dice:list):
    if all(elem in dice for elem in big1) == True:
        return True
    if all(elem in dice for elem in big2) == True:
        return True    
    return False

def yahtzee(dice:list):
    for x in range(1, 7):
        count_ = dice.count(str(x))
        if count_ == 5:
            return True
    return False

def totalcalc():
    global scoreDic
    scoreDic["total points"] = int(scoreDic.get("aces"))+int(scoreDic.get("twos"))+int(scoreDic.get("threes"))+int(scoreDic.get("fours"))+int(scoreDic.get("fives"))+int(scoreDic.get("sixes"))
    if scoreDic.get("total points") >= 63:
        scoreDic.update({"bonus": 35})
    scoreDic["total points 1"] = int(scoreDic.get("total points"))+int(scoreDic.get("bonus"))
    scoreDic["total points 2"] = int(scoreDic.get("three of a kind"))+int(scoreDic.get("four of a kind"))+int(scoreDic.get("full house"))+int(scoreDic.get("small straight"))+int(scoreDic.get("large straight"))+int(scoreDic.get("yahtzee"))+int(scoreDic.get("chance"))
    scoreDic["total"] = int(scoreDic.get("total points 1"))+int(scoreDic.get("total points 2"))


def scoreboard():
    totalcalc()
    print("part 1")
    print("aces: " + str(scoreDic.get("aces")))
    print("twos: " + str(scoreDic.get("twos")))
    print("threes: " + str(scoreDic.get("threes")))
    print("fours: " + str(scoreDic.get("fours")))
    print("fives: " + str(scoreDic.get("fives")))
    print("sixes: " + str(scoreDic.get("sixes")))
    print("total part 1: " + str(scoreDic.get("total points")))
    print("extra bonus: " + str(scoreDic.get("bonus")))
    print("total part 1: " + str(scoreDic.get("total points 1")))
    print("")
    print("")
    print("part 2")
    print("three of a kind: " + str(scoreDic.get("three of a kind")))
    print("four of a kind: " + str(scoreDic.get("four of a kind")))
    print("full house: " + str(scoreDic.get("full house")))
    print("small straight: " + str(scoreDic.get("small straight")))
    print("large straight: " + str(scoreDic.get("large straight")))
    print("yahtzee: " + str(scoreDic.get("yahtzee")))
    print("chance: " + str(scoreDic.get("chance")))
    print("total part 1: " + str(scoreDic.get("total points 1")))
    print("total part 2: " + str(scoreDic.get("total points 2")))
    print("total: " + str(scoreDic.get("total")))


game()
roll(stored)