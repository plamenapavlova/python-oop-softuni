def squares(n):
    for i in range(1, n + 1):
        yield i * i
        n =+ 1

print(list(squares(5)))