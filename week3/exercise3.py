"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
  
import random

def get_number(message):
    while True:
        try:
            answer = input(message)
            answer = int(answer)
            return answer
        except Exception:
            pass

def advancedGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    lowerBound = input("Enter an lower bound: ")
    print("OK then, a lower number is {}".format(lowerBound))
    lowerBound = int(lowerBound)
    upperBound = input("Enter an upper bound: ")
    print("OK then, a number between {} and {} ?".format(lowerBound,upperBound))
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(input("Guess a number: "))
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"

if __name__ == "__main__":
    print(advancedGuessingGame())
