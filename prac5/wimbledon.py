"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

function main
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)

function process_records(records)
    champion_to_count = {}
    countries = set(record[COUNTRY_INDEX] for record in records)
    for record in records
        champion_to_count[record[CHAMPION_INDEX]] = champion_to_count.get(record[CHAMPION_INDEX], 0) + 1
    return champion_to_count, countries

function display_results(champion_to_count, countries)
    display "Wimbledon Champions:"
    for name, count in champion_to_count.items()
        display name, count
    display len(countries)
    display (sorted(countries))

function get_records(filename)
    with open(filename, "r", encoding="utf-8-sig") as in_file
        in_file.readline()
        records = [line.strip().split(",") for line in in_file]
    return records
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Reads data file and prints details about Wimbledon champions and countries."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def process_records(records):
    """Creates a dictionary of champions and a set of countries from records."""
    champion_to_count = {}
    countries = set(record[COUNTRY_INDEX] for record in records)  # Uses set comprehension for unique countries

    for record in records:
        # Counts champions in the dictionary
        champion_to_count[record[CHAMPION_INDEX]] = champion_to_count.get(record[CHAMPION_INDEX], 0) + 1

    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Displays champions and countries."""
    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(f"{name} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def get_records(filename):
    """Gets records from the file in list of lists form."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        records = [line.strip().split(",") for line in in_file]

    return records


main()
