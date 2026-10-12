from abc import ABC, abstractmethod


class BasePainting(ABC):
    VALID_STATUSES = ("restorable", "irreparable", "ready")

    def __init__(self, catalogue_number: str, price:float, status:str):
        self.catalogue_number = catalogue_number
        self.price = price
        self.status = status

    @abstractmethod
    def restore(self):
        pass

    @property
    def catalogue_number(self):
        return self.__catalogue_number

    @catalogue_number.setter
    def catalogue_number(self, value):
        if not value.isdigit():
            raise ValueError("Invalid catalogue number!")
        self.__catalogue_number = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0.0:
            raise ValueError("Invalid price!")
        self.__price = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if value not in self.VALID_STATUSES:
            raise ValueError("Invalid status!")
        self.__status = value

    @property
    def is_ready(self):
        return self.status == "ready"
    


