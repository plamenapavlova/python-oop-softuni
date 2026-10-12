class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current = count + 1


    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 0:
            self.current -= 1
            return self.current
        else:
            raise StopIteration


iterator = countdown_iterator(10)

for item in iterator:
    print(item, end=" ")