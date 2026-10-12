from .animal import Animal


class Lion(Animal):
    def __init__(self, name:str, age:str, gender:int):
        super().__init__(name, age, gender, 50)