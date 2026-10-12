def reverse_text(text: str):
    digits = len(text) - 1
    for i in range (digits, -1, -1):
        yield text[i]


for char in reverse_text("step"):
    print(char, end='')