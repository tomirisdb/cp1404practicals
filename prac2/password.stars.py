"""
function main
    MIN_LENGTH = 8
    get password
    password = get_password(MIN_LENGTH, password)
    print_asterisks(password)

function print_asterisks(password)
    display len(password) * "*"

function get_password(MIN_LENGTH, password)
    while len(password) < MIN_LENGTH
        display "Invalid password length. Try again"
        get password
    return password
"""


def main():
    MIN_LENGTH = 8
    password = input("Enter password: ")
    password = get_password(MIN_LENGTH, password)
    print_asterisks(password)


def print_asterisks(password):
    print(len(password) * "*")


def get_password(MIN_LENGTH, password):
    while len(password) < MIN_LENGTH:
        print("Invalid password length. Try again")
        password = input("Enter password: ")
    return password


main()
