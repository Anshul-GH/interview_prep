# iterative approach
def iterative_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact


def recursive_factorial(n):
    if n == 1:
        return n
    else:
        temp = recursive_factorial(n-1)
        return temp * n


def main():
    # print(iterative_factorial(5))
    print(recursive_factorial(5))


if __name__ == "__main__":
    main()
