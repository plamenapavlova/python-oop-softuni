class Room:
    def __init__(self, number:int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken:bool = False

    def take_room(self, people):
        if self.is_taken == False and self.capacity >= people:
            self.is_taken = True
        return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken == True:
            self.is_taken = False
        return f"Room number {self.number} is not taken"