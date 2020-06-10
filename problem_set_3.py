"""
Exam #1 / Problem set #3.
Your job is to complete the definitions of each function mentioned in the comments
so that it achieves its indicated behavior.

Do not run this file directly.
Run the file named main.py if you want to try out the code in these functions.
"""

import random

##--------------------- Function #1 ---------------------##
# Define a function named 'get_die' that rolls an imaginary die
#   and returns a pseudo-random integer in the range from 1 to 6, inclusive.
# This function must not accept any arguments.
# Use the function random.randint() to generate the pseudo-random number.

def get_die():
    die = random.randint(1,6)
    return die

##--------------------- Function #2 ---------------------##
# Define a function named 'get_die_in_range' that rolls an imaginary die
#   and returns a pseudo-random integer in a given range.
# This function must accept two arguments: the low and high boundaries to use
#   for the pseudo-random number that is returned.
# E.g., if the function is passed a 2 and a 7, the pseudo-random integer
#   should be between 2 and 7, inclusive.
# Use the function random.randint() to generate the pseudo-random number.

def get_die_in_range():
    low = int(input("What is your low boundary: "))
    high = int(input("What is your high boundary: "))
    die1 = random.randint(low-1,high)
    return die1

##--------------------- Function #3 ---------------------##
# Define a function named 'play_four' that rolls four imaginary dice.
# The function always prints, "You rolled a 12!", where 12 is 
#   replaced with the actual sum of the four virtual dice.
# Additionally, if the values of the four dice are all 1, the function
#   prints "Four eyes!"
# Additionally, if the values of the dice add up to over 21, the function
#   prints, "Bust!"
# 
# You must use the 'get_die' function defined above to roll 2 of the virtual dice.
# You must use the 'get_die_in_range' function defined above to roll the other 2 of
#   the virtual dice, with a range between 1 and 7.

def play_four():


    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    die_3 = random.randint(1,6)
    die_4 = random.randint(1,6)

    sum = die_1 + die_1 + die_3 + die_4
    print("You rolled a {}!".format(sum))
    if 3 < sum < 5
        print("Four eyes!")
    elif sum > 21
        print("Bust!")
    else:
        print("You rolled a {}!".format(sum))
    return play_four