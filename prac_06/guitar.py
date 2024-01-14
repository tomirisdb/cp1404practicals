"""
Estimated time:
Actual time:
Pseudocode:
class Guitar
    function __init__(self, name="", year=0, cost=0)
        self.name = name
        self.year = year
        self.cost = cost

    function __str__(self)
        return self.name, self.year, self.cost

    function get_age(self)
        return CURRENT_YEAR - self.year

    function is_vintage(self)
        return self.get_age() >= VINTAGE_AGE
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

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not based on age."""
        return self.get_age() >= VINTAGE_AGE
