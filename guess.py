import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Too high")
        elif guess < random_number:
            print("Too low")
    print("You win!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if high != low:
            guess = random.randint(low, high)
            feedback = input(f"{guess} (h, l, c): ")

            if feedback == "h":
                high = guess - 1
            elif feedback == "l":
                low = guess + 1
            elif feedback == "c":
                print("Yay!")
            else:
                print("error")
        else:
            print(f"Definitely {high}")
            feedback = "c"

        
computer_guess(10)