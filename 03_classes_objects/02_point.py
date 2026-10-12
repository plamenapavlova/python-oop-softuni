class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_x(self, new_y):
        self.x = new_y

    def __str__(self):
        return f"The point has coordinates ({self.x}, {self.y})"

