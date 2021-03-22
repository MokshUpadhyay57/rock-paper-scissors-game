import random   # imports random module

# Game function 
def gameWin(user,computer):
    if (user == 'r' and computer == 's') or (user =='s' and computer =='p') or(user == 'p' and computer =='r'):
        return True
    else:
        return False

def play():
    # Computer's Turn
    computer = random.choice(['r','p','s'])

    # User Turn
    user  = input("Your's turn: Rock(r), Paper(p) and Scissor(s)?")

    # These lines print the choices.
    print("Computer Choose: " + computer)
    print("You Choose: " + user)
    
    # Checking whose winning
    if user == computer:
        return 'It\'s a tie.'
    if gameWin(user,computer):
        return 'You Won!!!' 
    return 'You Lost...'

print(play())