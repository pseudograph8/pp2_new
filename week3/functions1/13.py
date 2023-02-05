'''
Write a program able to play the "Guess the number" - game, where the number to be guessed is 
randomly chosen between 1 and 20. This is how it should work when run in a terminal:
    Hello! What is your name?
    KBTU

    Well, KBTU, I am thinking of a number between 1 and 20.
    Take a guess.
    12

    Your guess is too low.
    Take a guess.
    16

    Your guess is too low.
    Take a guess.
    19

14. Good job, KBTU! You guessed my number in 3 guesses!
''' 
import random

def sen():
    print("Take a guess.")


print("Hello! What is your name?")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
sen()

ran = random.randint(1, 20)


count = 0

while count<20:
    count += 1
    guess = int(input())
    if guess == ran:
        print(f"Good job, {name}! You guessed my number in {count} guesses!")
        break
    elif guess>ran:
        print("Your guess is too high.")
        sen()
    elif guess<ran:
        print("Your guess is too low.")
        sen()
'''
print(ran)
'''