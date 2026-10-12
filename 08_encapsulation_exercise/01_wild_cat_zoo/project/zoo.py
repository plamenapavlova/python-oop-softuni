from .animal import Animal
from .worker import Worker


class Zoo:
    def __init__(self, name:str, budget:int, animal_capacity:int, workers_activity:int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_activity = workers_activity
        self.animals:list[Animal] = []
        self.workers:list[Worker] = []

    def add_animal(self, animal: Animal, price) -> str:
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.name} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) >= self.__workers_activity:
            return "Not enough space for worker"
        return f"{worker.name} the {worker.__class__.name} hired successfully"

    def fire_worker(self, worker_name:str) -> str:
        worker = next((for worker in self.workers if worker_name == worker.name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum(w.salary for w in self.workers)
        if total_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        total_money_for_care = sum(a.money_for_care for a in self.animals)
        if total_money_for_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount:int) -> None:
        self.__budget += amount

    def animal_status(self):
        return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")

    def workers_status(self):
        return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")

    def __print_status(self, collection_ls: list[Animal|Worker], *args: str):
        elements ={arg: [] for arg in args} #{ "Lion": []}
        for item in collection_ls:
            elements[item.__class__.__name__].append(repr(item))

        result = [f"You have {len(collection_ls)} {str(collection_ls[0].__class__.__bases__[0].__name__.lower)}s"]
        for key, value in elements.items():
            result.append(f"----- {len(value)} {key}s:")
            result.extend(value)

        return "\n".join(result)















