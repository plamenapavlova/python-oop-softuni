class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.current = -1
        self.length = len(sequence)

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current <= self.number:
            return self.sequence[self.current % self.length]
        else:
            raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

print("")
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')