class Vehicle:
    DEFAULT_FUEL_CONSUMPTION:float = 1.25
    fuel_consumption:float

    def __init__(self, fuel: float, horse_power:int):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers: int):
        consumed_fuel = kilometers * self.fuel_consumption
        if self.fuel >= consumed_fuel:
            self.fuel -= consumed_fuel