"""
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
RANDOM_NUMBERS_PER_LINE = 6

function main
    get number_of_quick_picks
    while number_of_quick_picks < 0
        display "Invalid input"
        get number_of_quick_picks

      for i in range(number_of_quick_picks)
        quick_pick = []
        for j in range(RANDOM_NUMBERS_PER_LINE)
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number in quick_pick
                number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            add number to quick_pick
        quick_pick.sort()
        display number for number in quick_pick
"""
import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
RANDOM_NUMBERS_PER_LINE = 6


def main():
    """Gets user input and chooses random numbers"""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid input")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(RANDOM_NUMBERS_PER_LINE):
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number in quick_pick:
                number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()


