from .id_mixin import IdMixin


class ExercisePlan(IdMixin):
    def __init__(self, trainer_id, equipment_id, duration:int):#duration in minutes
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()
        self.increment_id()

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        duration = hours *60
        return cls(trainer_id, equipment_id, duration)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"


