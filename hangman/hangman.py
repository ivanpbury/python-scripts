from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    correct_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left. Used letters: ", " ".join(used_letters))

        word_list = []
        for letter in word:
            if letter in correct_letters:
                word_list.append(letter)
            else:
                word_list.append("-")
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet and user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                correct_letters.add(user_letter)

            else:
                lives -= 1
                print("Letter is not in word.")
        
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You lose. The word was", word)
    else:
        print("You guessed the word!")

hangman()

