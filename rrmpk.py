import random
tools = ["rani","mantri","police","Kalla"]
print("RAJA RANI MANTRI POLICE KALLA")
print("You are RAJA, find RANI")
comp1=random.choice(tools)
tools.remove(comp1)
comp2=random.choice(tools)
tools.remove(comp2)
comp3=random.choice(tools)
tools.remove(comp3)
comp4=random.choice(tools)
tools.remove(comp4)
i=10000
print(comp1)
print(comp2)
print(comp3)
print(comp4)
while(True):
    choice=input("Is it comp1/2/3/4: ")
    if choice == "comp1" and comp1 == "rani":
        print("You found RANI ")
        break
    elif choice == "comp2" and comp2 == "rani":
        print("You found RANI ")
        break
    elif choice == "comp3" and comp3 == "rani":
        print("You found RANI ")
        break
    elif choice == "comp4" and comp4 == "rani":
        print("You found RANI ")
        break
    else:
        print("Try again")
        i=i-100
print("Now that you found Rani now find mantri")
print("Now your points is ",i)
while(True):
    choice=input("Is it comp1/2/3/4: ")
    if choice == "comp1" and comp1 == "mantri":
        print("You found MANTRI ")
        break
    elif choice == "comp2" and comp2 == "mantri":
        print("You found MANTRI ")
        break
    elif choice == "comp3" and comp3 == "mantri":
        print("You found MANTRI ")
        break
    elif choice == "comp4" and comp4 == "mantri":
        print("You found MANTRI ")
        break
    else:
        print("Try again")
        i=i-100
print("Now that you found MANTRI now find police")
print("Now your points is ",i)
while(True):
    choice=input("Is it comp1/2/3/4: ")
    if choice == "comp1" and comp1 == "police":
        print("You found POLICE ")
        break
    elif choice == "comp2" and comp2 == "police":
        print("You found POLICE ")
        break
    elif choice == "comp3" and comp3 == "police":
        print("You found POLICE ")
        break
    elif choice == "comp4" and comp4 == "police":
        print("You found POLICE ")
        break
    else:
        print("Try again")
        i=i-100
print("Now that you found POLICE now find kalla")
print("Now your points is ",i)
while(True):
    choice=input("Is it comp1/2/3/4: ")
    if choice == "comp1" and comp1 == "kalla":
        print("You found KALLA ")
        break
    elif choice == "comp2" and comp2 == "kalla":
        print("You found KALLA ")
        break
    elif choice == "comp3" and comp3 == "kalla":
        print("You found KALLA ")
        break
    elif choice == "comp4" and comp4 == "kalla":
        print("You found KALLA ")
        break
    else:
        print("Try again")
        i=i-100
print("CONGRATULATIONS!!! \a YOU \a HAVE COMPLETED THE GAME \a")
print("Now your TOTAL POINTS is ",i)