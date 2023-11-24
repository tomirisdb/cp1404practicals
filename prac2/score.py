"""
HIGH_GRADE = 90
LOW_GRADE = 50

function main
    get score
     while score < 0 or score > 100
        display "Invalid score"
        get score
    display display_score(score)
    random_score = random.randint(LOW_GRADE, HIGH_GRADE)
    display random_score

function display_score
    if score >= HIGH_GRADE
        return "Excellent"
    else if score >= LOW_GRADE
        return "Passable"
    else
        return "Bad"
"""
import random

HIGH_GRADE = 90
LOW_GRADE = 50


def main():
    """Get user input and print random score"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(display_score(score))

    random_score = random.randint(LOW_GRADE, HIGH_GRADE)
    print(f'Random score: {random_score}')


def display_score(score):
    """display scores"""
    if score >= HIGH_GRADE:
        return "Excellent"
    elif score >= LOW_GRADE:
        return "Passable"
    else:
        return "Bad"


main()
