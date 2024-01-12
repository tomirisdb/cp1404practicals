"""
TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
MENU = "q)uit, c)hoose taxi, d)rive"


function main()
    bill = 0.00
    display "Let's drive!"
    is_finished = False
    current_taxi = None
    while not is_finished
        print(MENU)
        get choice
        if choice == 'q'
            display bill
            display 'Taxis are now:'
            display_taxis()
        else if choice == 'c'
            current_taxi = choose_taxi()
        else if choice == 'd'
            bill += drive_taxi(current_taxi)
        else
            display Invalid option"
            display bill

function drive_taxi(current_taxi)
    if current_taxi is None
        display 'You need to choose a taxi before you can drive'
        return 0
    get distance
    current_taxi.start_fare()
    current_taxi.drive(distance)
    display current_taxi.name, current_taxi.get_fare()
    return current_taxi.get_fare()


function choose_taxi()
    display "Taxis available: "
    display_taxis()
    get choice_taxi
    if choice_taxi < 0 or choice_taxi > len(TAXIS) - 1
        display "Invalid taxi choice"
        return None
    return TAXIS[choice_taxi]


def display_taxis()
    i = 0
    for taxi in TAXIS
        display i, taxi
        i = i + 1
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    bill = 0.00
    print("Let's drive!")
    is_finished = False
    current_taxi = None
    while not is_finished:
        print(MENU)
        choice = input('>>> ').lower().strip()
        if choice == 'q':
            print(f'Total trip cost: ${bill:.2f}')
            print('Taxis are now:')
            display_taxis()
        elif choice == 'c':
            current_taxi = choose_taxi()
        elif choice == 'd':
            bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f'Bill to date: ${bill:.2f}')


def drive_taxi(current_taxi):
    if current_taxi is None:
        print('You need to choose a taxi before you can drive')
        return 0
    distance = int(input('Drive how far? '))
    current_taxi.start_fare()
    current_taxi.drive(distance)
    print(f'Your {current_taxi.name} trip cost you ${current_taxi.get_fare()}')
    return current_taxi.get_fare()


def choose_taxi():
    print("Taxis available: ")
    display_taxis()
    choice_taxi = int(input('Choose taxi: '))
    if choice_taxi < 0 or choice_taxi > len(TAXIS) - 1:
        print("Invalid taxi choice")
        return None
    return TAXIS[choice_taxi]


def display_taxis():
    i = 0
    for taxi in TAXIS:
        print(f"{i} - {taxi}")
        i += 1


if __name__ == '__main__':
    main()
