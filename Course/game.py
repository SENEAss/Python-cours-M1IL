#the game of + or -
from random import randint

print("1. Easy level: 0-10")
print("2. Medium level: 0-100")
print("3. Difficult level: 0 - 1000")
print("4. Quit")

choice = int(input("Enter your choice for the level : "))
coups = 1
x_choice1 =randint(0,10)
x_choice2 =randint(0,100)
x_choice3 =randint(0,1000)

if choice == 1:
    n = int(input("veuillez entrer un nombre: "))
    while n != x:
        if n<x:
            print("le nombre à deviner est plus grand !")
        elif n>x:
            print("le nombre à deviner est plus grand !")
        else :
            print("Bravo, vous avez trouver le nombre qu'il fallait deviner")
    """elif choice == 2:
        n = int(input("veuillez entrer un nombre: "))
        x=randint(0,100)
        while n != x:
            if n<x:
                print("le nombre à deviner est plus grand !")
            else:
                print("le nombre à deviner est plus grand !")
                
            n = int(input("veuillez entrer un nombre: "))
            coups +=1
            print("Bravo, vous avez trouver le nombre qu'il fallait deviner")
    elif choice == 3:
        n = int(input("veuillez entrer un nombre: "))
        x=randint(0,1000)
        while n != x:
            if n<x:
                print("le nombre à deviner est plus grand !")
            elif n>x:
                print("le nombre à deviner est plus grand !")
            else :
                print("Bravo, vous avez trouver le nombre qu'il fallait deviner")"""
elif choice == 4:
    quit()
else:
    print("Invalid choice")
        
        
 #A corriger