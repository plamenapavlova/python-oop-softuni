def fibonacci():
    cur_num, next_num = 0, 1
    while True:
        yield cur_num
        cur_num, next_num =  next_num, cur_num + next_num


generator = fibonacci()

for i in range(10):
    print(next(generator))