from taxi import Taxi

class SilverServiceTaxi(Taxi):

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name, fuel)
        self.fanciness = fanciness * Taxi.price_per_km

    def get_fare(self):
        return self.fanciness * self.current_fare_distance + self.flagfall

    def __str__(self):
        return super().__str__() + " plus flagfall of $4.50," + f" price: ${self.get_fare()}"
