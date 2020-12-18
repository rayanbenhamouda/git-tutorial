#! /usr/bin/python3
 
# The random package is needed to choose a random number
import random
 
# Define the game in a function
def guess_loop():
    pseudo = input("enter your username: ")
    # This is the number the user will have to guess, chosen randomly in between 1 and 100
    nbr_essaie = 5
    number_to_guess = random.randint(1, 50)
    print("I have in mind a number in between 1 and 50, can you find it?")
    print("you have 5 tries")
    # Replay the question until the user finds the correct number
    while True:
        try:
            # Read the number the user inputs
            guess = int(input())
            # Compare it to the number to guess
            if guess > number_to_guess:
                print("The number to guess is lower")
                nbr_essaie = nbr_essaie-1
                if nbr_essaie == 0:
                    print("number of tests awaits, you've lost to the game: ",pseudo,", the number was:",number_to_guess)
                    return
            elif guess < number_to_guess:
                print("The number to guess is higher")
                nbr_essaie = nbr_essaie-1 
                if nbr_essaie == 0:
                    print("number of tests awaits, you've lost to the game: ",pseudo,", the number was:",number_to_guess)
                    return
            else:
                # The user found the number to guess, let's exit
                print("You just found the number, it was indeed", guess)
                print("play well", pseudo) 
                return
        # A ValueError is raised by the int() function if the user inputs something else than a number
            print("number of trials remaining:", nbr_essaie)

        except ValueError as err:
            print("Invalid input, please enter an integer")
 
# Launch the game
guess_loop()
