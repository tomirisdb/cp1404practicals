"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the user will enter other data types other than integer.
2. When will a ZeroDivisionError occur?
When the user will enter 0 as a denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, we can use while loop to check is the input valid or not.
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Can not divide by zero. Try again!")
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

