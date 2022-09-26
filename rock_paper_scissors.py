import random

def play():
    user = input("r, p, or s? ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        print("tie")
    elif is_win(user, computer):
        print("You win!")
    else:
        print("You lose.")

def is_win(user, computer):
        if (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
            return True
        else:
            return False

play()