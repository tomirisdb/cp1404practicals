HIGH_GRADE = 90
LOW_GRADE = 50


def main():
    MENU = "(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    score = get_valid_score()
    print(MENU)
    choice = input("").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(print_scores(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("").upper()
    print("Farewell.")


def get_valid_score():
    """Gets valid score"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.")
        score = int(input("Enter score: "))
    return score


def print_scores(score):
    """Displays scores"""
    if score >= HIGH_GRADE:
        return "Excellent"
    elif score >= LOW_GRADE:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Shows stars"""
    stars = "*" * score
    print(stars)


main()


