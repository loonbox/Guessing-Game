"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

import random
import statistics
import sys

from statistics import mean, mode, median

attempts =[]

def play_again():
    play_again = input("Would you like to play again? Y for yes N for no ")
    if play_again == "Y":
        start_game()
    elif play_again == "N":
        print("**********Goodbye**********")
        sys.exit()

def start_game():
    number = random.randint(1,10)
    number_of_picks = 0
    print("************ Welcome To The Guessing Game ****************")
    while True:
        try:
            guess = int(input("Pick a number between 1 and 10: "))

            if guess == number:
                print("Got it!")
                number_of_picks += 1
                print("It took {} number of picks to get the answer".format(number_of_picks))
                attempts.append(number_of_picks)

                mean_of_chances = mean(attempts)
                print("This is the mean: ", mean_of_chances)

                median_of_chances = median(attempts)
                print("This is the median: ", median_of_chances)

                mode_of_chances = mode(attempts)
                print("This is mode: ", mode_of_chances)

                play_again()
                break

            elif guess < number:
                print("It's higher")
                number_of_picks += 1


            elif guess > number:
                print("It's lower")
                number_of_picks += 1


        except ValueError:
            print("Please Use Only Numbers")


        print("Number of Picks: {}".format(number_of_picks))



start_game()
