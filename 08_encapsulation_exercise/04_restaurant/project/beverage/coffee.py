from project.beverage import Beverage


class Coffee(Beverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name, caffeine:float):
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
