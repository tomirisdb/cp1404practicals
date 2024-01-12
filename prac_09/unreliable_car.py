from prac_09.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, fuel, name, reliability: float):
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        if randint(0, 100) > self.reliability:
            print("Car broke!")
            return
        super().drive(distance)


