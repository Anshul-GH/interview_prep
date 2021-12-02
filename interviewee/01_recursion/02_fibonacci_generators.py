def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

generator = fibonacci_sequence()
for i in range(10):
    print(next(generator))
