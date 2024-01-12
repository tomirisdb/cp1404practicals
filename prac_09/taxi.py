"""
CP1404/CP5632 Practical
Car class
Pseudocode:
class Taxi(Car)
    price_per_km = 1.23
    function __init__(self, name, fuel)
        super().__init__(fuel, name)
        self.current_fare_distance = 0

    function __str__(self)
        return self.current_fare_distance, self.price_per_km

    function get_fare(self)
        return self.price_per_km * self.current_fare_distance

    function start_fare(self)
        self.current_fare_distance = 0

    function drive(self, distance)
        self.current_fare_distance =  self.current_fare_distance + super().drive(distance)
        return self.current_fare_distance
"""
from prac_09.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    price_per_km = 1.23

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(fuel, name)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} {self.current_fare_distance} km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        self.current_fare_distance += super().drive(distance)
        return self.current_fare_distance
