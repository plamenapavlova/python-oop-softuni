import re
from abc import ABC, abstractmethod
from astronauts.base_astronaut import BaseAstronaut


class BaseStation(ABC):
    def __init__(self, name:str, capacity:int):
        self.name = name
        self.capacity = capacity
        self.astronauts:list[BaseAstronaut] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if re.fullmatch(r"[A-Za-z0-9-]+", value) is None:
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self):
        total_salary = 0
        for a in self.astronauts:
            total_salary += a.salary
        return f"{total_salary:.2f}"

    def status(self):
        if not self.astronauts:
            austronaut_ids = 'N/A'
        else:
            austronaut_ids = ' #'.join(sorted(a.id_number for a in self.astronauts))
        return f"Station name: {self.name}; Astronauts: {austronaut_ids}; Total salaries: {self.calculate_total_salaries()}"

    @abstractmethod
    def update_salaries(self, min_value:float):
        pass