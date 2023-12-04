"""
function main
    display MENU
    get choice
    while choice != "Q"
        if choice == "C"
            get celsius
            result = celsius_to_fahrenheit(celsius)
            display result
        else if choice == "F"
            get fahrenheit
            result = fahrenheit_to_celsius(fahrenheit)
            display result
        else
            display "Invalid option"
        display MENU
        get choice
    display thank you message

function celsius_to_fahrenheit(celsius)
    return celsius * 9.0 / 5 + 32

function fahrenheit_to_celsius(fahrenheit)
    return 5 / 9 * (fahrenheit - 32)
"""


def main():
    """Gets user input, validates user input and displays results"""
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)

    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            result = celsius_to_fahrenheit(celsius)
            print(f"Result: {result:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            result = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {result:.2f} C")
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    """Converts celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Converts fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)


main()


