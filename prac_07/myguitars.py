"""
Estimated time: 30 minutes
Actual time: 30 minutes
Pseudocode:
class Guitar
    function __init__(self, name="", year=0, cost=0)
        self.name = name
        self.year = year
        self.cost = cost

    function __str__(self)
        return self.name, self.year, self.cost

    function __lt__(self, other)
        return self.year < other.year

    function get_age(self)
        return CURRENT_YEAR - self.year

    function is_vintage(self)
        return self.get_age() >= VINTAGE_AGE

guitars_list = []
with open("guitars.csv", "r") as file
    for line in file
        parts = line.strip().split()
        name, year, cost = parts[0], int(parts[1]), float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars_list.append(guitar)


display "Guitars:"
for guitar in guitars_list
    print(guitar)

guitars_list.sort()


display "Guitars (oldest to newest):"
for guitar in guitars_list
    print(guitar)

while True
    get name
    if name.lower() == 'quit'
        break
    get year
    get cost
    new_guitar = Guitar(name, year, cost)
    guitars_list.append(new_guitar)


with open("guitars.csv", "w") as file
    for guitar in guitars_list
        file.write guitar.name, guitar.year,guitar.cost


display "All Guitars:"
for guitar in guitars_list
    print(guitar)
"""

CURRENT_YEAR = 2017
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Enable comparison of Guitars based on their years."""
        return self.year < other.year

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not based on age."""
        return self.get_age() >= VINTAGE_AGE


# Read guitars from guitars.csv and store them in a list of Guitar objects
guitars_list = []
with open("guitars.csv", "r") as file:
    for line in file:
        parts = line.strip().split(',')
        name, year, cost = parts[0], int(parts[1]), float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars_list.append(guitar)

# Display guitars using a loop
print("Guitars:")
for guitar in guitars_list:
    print(guitar)

# Sort the list by year (oldest to newest) using the defined __lt__ method
guitars_list.sort()

# Display sorted guitars
print("\nGuitars (oldest to newest):")
for guitar in guitars_list:
    print(guitar)

# Ask the user to enter new guitars
while True:
    name = input("Enter the name of the guitar (or 'quit' to stop): ")
    if name.lower() == 'quit':
        break
    year = int(input("Enter the year of manufacture: "))
    cost = float(input("Enter the cost of the guitar: "))
    new_guitar = Guitar(name, year, cost)
    guitars_list.append(new_guitar)

# Write all guitars to the data file guitars.csv
with open("guitars.csv", "w") as file:
    for guitar in guitars_list:
        file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

# Display all guitars (existing + new)
print("\nAll Guitars:")
for guitar in guitars_list:
    print(guitar)
