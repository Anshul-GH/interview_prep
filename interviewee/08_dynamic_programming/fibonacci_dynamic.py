# create a function fib(n) that returns the nth value of the fibonacci series
# fibonacci_series = 1, 1, 2, 3, 5, 8, 13, 21 ...

def fib(n, memo={}):
    # base case
    if n <= 2:
        return 1
    
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]


if __name__ == "__main__":
    n = int(input("Element of fibonacci series to be generated:"))
    print(fib(n))
