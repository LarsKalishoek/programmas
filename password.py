import random

alphabet     = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
speciallist  = ['@', '#', '$', '%', '&', '_', '?']
nummer      = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

upper = random.randint(2, 7)
lower = 8
numberAmount = random.randint(4, 8)
special = 3
total = upper + lower + numberAmount + special

def passList(up, low, num, tot):
    while tot < 24:
        choice = random.randint(0, 3)
        if choice == 0 and up < 6:
            global upper
            upper += 1
            tot += 1
        elif choice == 1:
            global lower
            lower += 1
            tot += 1
        elif choice == 2 and num < 7:
            global numberAmount
            numberAmount += 1
            tot += 1

def addList(up, low, num, special):
    passwordList = []
    for x in range(0, up):
        passwordList.append(random.choice(alphabet).upper())
    for x in range(0, low):
        passwordList.append(random.choice(alphabet))
    for x in range(0, special):
        passwordList.append(random.choice(speciallist))
    for x in range(0, num):
        passwordList.append(random.choice(nummer))
    return passwordList

def check(password):
    random.shuffle(password)
    while password[0] in speciallist or password[23] in speciallist or password[0] in nummer or password[1] in nummer or password[2] in nummer: 
        random.shuffle(password)
    print(*password, sep='')
passList(upper, lower, numberAmount, total)
password = addList(upper, lower, numberAmount, special)
check(password)