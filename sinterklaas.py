import random
nameList = []
copyList1 = []
copyList2 = []
nameSets = {}
print("type klaar als alle namen ingevoerd zijn")

def inputName():
    global nameList
    name = input("Wat is jouw naam?: ").capitalize()
    if name in nameList:
        print("deze naam is al ingevoerd!")
        inputName()
    if name == "Klaar" and len(nameList) >= 2:
        shuffleLists()
    nameList.append(name)
    inputName()

def shuffleLists():
    x = 1
    y = 1
    global copyList1
    global copyList2
    copyList1 = nameList.copy()
    copyList2 = nameList.copy()
    while len(copyList1) != 0:
        x = 1
        y = 1
        while x == y and len(copyList1) > 1:
            x = random.choice(copyList1)
            y = random.choice(copyList2)
        if len(copyList1) == 1:
            if copyList1[0] == copyList2[0]:
                shuffleLists()
            else:
                x = copyList1[0]
                y = copyList2[0]
        copyList1.remove(x)
        copyList2.remove(y)
        nameSets[x] = y
    print(nameSets)
    input()
    exit()

inputName()
