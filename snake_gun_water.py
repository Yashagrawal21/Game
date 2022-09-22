import random

def gameWin(comp, you):
    if comp == you:
        return None

    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    elif comp == 'w':            
        if you == 'g':
            return False
        elif you == 's':
            return True

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True 

print("Comp Turn: Snake(s) Water(w) Gun(g)")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g' 


you = input("Your Turn: Snake(s) Water(w) Gun(g)\n")
a = gameWin(comp, you)

print(f"Computer Choice: {comp}")
print(f"Your Choice: {you}")

if a == None:
    print("Game is Tie!")
elif a:
    print("You win")
else:
    print("You Lose")        