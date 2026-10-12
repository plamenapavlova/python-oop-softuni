from .customer import Customer
from .dvd import DVD


class MovieWorld:
    def __init__(self, name:str):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id:int, dvd_id:int):
        cust = next((c for c in self.customers if customer_id == c.id), None)
        dvd = next((d for d in self.dvds if dvd_id == d.id), None)
        if dvd in cust.rented_dvds:
            return f"{cust.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return f"DVD is already rented"
        if cust.age < dvd.age_restriction:
            f"{cust.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        cust.rented_dvds.append(dvd)
        return f"{cust.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        cust = next((c for c in self.customers if customer_id == c.id), None)
        dvd = next((d for d in cust.rented_dvds if dvd_id == d.id), None)
        if dvd in cust.rented_dvds:
            cust.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{cust.name} has successfully returned {dvd.name}"
        return f"{cust.name} does not have that DVD"

    def __repr__(self):
        result = "\n".join([c.__repr__() for c in self.customers]) + "\n"
        result += "\n".join([d.__repr__() for d in self.dvds])
        return result