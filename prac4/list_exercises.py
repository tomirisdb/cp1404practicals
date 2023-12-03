"""
function quick_program_1
    numbers = []
    for i in range(5)
        get number
        add number to numbers
    display numbers

    display numbers[0]
    display numbers[-1]
    display min(numbers)
    display max(numbers)
    display sum(numbers) / len(numbers)
"""


def quick_program_1():
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    print(numbers)

    print(f'The first number is {numbers[0]}')
    print(f'The last number is {numbers[-1]}')
    print(f'The smallest number is {min(numbers)}')
    print(f'The largest number is {max(numbers)}')
    print(f'The average of the numbers is {sum(numbers) / len(numbers):.1f}')


quick_program_1()


"""
function quick_program_2
    usernames = list
    get username
    if username in usernames
        message = "Access granted"
    else
        message = "Access denied"
    display message 
"""


def quick_program_2():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Enter your name: ")
    if username in usernames:
        message = "Access granted"
    else:
        message = "Access denied"
    print(message)


quick_program_2()
