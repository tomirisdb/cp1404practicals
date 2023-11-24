"""
CP1404/CP5632 - Practical
Broken program to determine score status
Pseudocode:
HIGH_GRADE = 90
LOW_GRADE = 50
get score
while score < 0 or score > 100
    display "Invalid score"
    get score
if score >= HIGH_GRADE
    display "Excellent"
else if score >= LOW_GRADE
    display "Passable"
else
    display "Bad"
"""
# TODO: Fix this!
HIGH_GRADE = 90
LOW_GRADE = 50
score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))
if score >= HIGH_GRADE:
    print("Excellent")
elif score >= LOW_GRADE:
    print("Passable")
else:
    print("Bad")
