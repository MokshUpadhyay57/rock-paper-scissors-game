import random
from time import sleep
def gameWin(a,b):
    if a == 'r':
        if b == 'p':
            return True
        elif b == 's':
            return False
        else:
            return None
    if a == 'p':
        if b == 'r':
            return False
        elif b == 's':
            return True
        else:
            return None
    if a == 's':
        if b == 'p':
            return False
        elif b == 'r':
            return True
        else:
            return None      
a = print("Computer's turn: Rock(r), Paper(p) and Scissor(s)?")
randNo = random.randint(1,3)
if randNo == 1:
    a = 'r'
elif randNo == 2:
    a = 'p'
elif randNo ==3:
    a ='s'

sleep(1)
b  = input("Your's turn: Rock(r), Paper(p) and Scissor(s)?")
print("Computer Choose: " + str(a))

print("You Choose: " + str(b))
g = gameWin(a,b)
if g == None:
    print("Tie")
elif g:
    print("You Won!!!")
else:
    print("You Lose...")