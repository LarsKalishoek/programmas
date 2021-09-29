slaap = 1

def generateLijst():
    boodschappen = {}
    while slaap != 0:
        lijst = input("Wat wilt u toevoegen aan uw boodschappen lijst? : ").lower()
        aantal = int(input("Hoeveel wilt u hiervan?  : "))
        if lijst in boodschappen:
            boodschappen[lijst] += aantal
        else:
            boodschappen.update({lijst : aantal })     
        vraag = input("Wilt u nogmeer toevoegen Y/N  : ").lower()
        if vraag == "y":
            pass
        else:
            print(boodschappen)
            break

generateLijst()