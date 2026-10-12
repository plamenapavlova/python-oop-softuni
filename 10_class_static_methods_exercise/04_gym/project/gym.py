from .customer import Customer
from .equipment import Equipment
from .exercise_plan import ExercisePlan
from .subscription import Subscription
from .trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions:list[Subscription] = []

    def add_customer(self, customer:Customer):
        self.__add_object(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_object(trainer, self.trainers)

    def add_equipment(self, equipment:Equipment):
        self.__add_object(equipment, self.equipment)

    def add_plan(self, plans: ExercisePlan):
        self.__add_object(plans, self.plans)

    def add_subscription(self, subscription:Subscription):
        self.__add_object(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer = next((c for c in self.customers if c.id == subscription.customer_id), None)
        trainer = next((t for t in self.trainers if t.id == subscription.trainer_id), None)
        plan = next((p for p in self.plans if p.id == subscription.exercise_id), None)
        equipment = next((e for e in self.equipment if e.id == plan.equipment_id), None)

        return "\n".join([subscription.__repr__(),
                         customer.__repr__(),
                        trainer.__repr__(),
                        equipment.__repr__(),
                        plan.__repr__()])

    @staticmethod
    def __add_object(obj, col) -> None:
        if obj not in col:
            col.append(obj)