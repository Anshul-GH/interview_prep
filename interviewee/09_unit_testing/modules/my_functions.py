# simple function to multiply two integers
def multiply_two_numbers(x, y):
    return sum(y for _ in range(x))

# simple function to multiply two integers
def multiply_two_numbers_better(x, y):
    # return sum(y for _ in range(x))
    if (x >= 0 and y >= 0) or (x < 0 and y < 0):
        return sum(abs(y) for _ in range(abs(x)))
    elif x < 0:
        return sum(x for _ in range(y))
    else:
        return sum(y for _ in range(x))
