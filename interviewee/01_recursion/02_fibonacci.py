# Fibonacci: Sum of the last two numbers gives the next one.
# Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 .....
# Works only with positive integers

# Step1: Recursive Case
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

# Step2: Base Case
# fibonacci(0) = 0
# fibonacci(1) = 1

# Step3: Edge Cases or Constraints
# Only positive integers
# fibonacci(-1) ??
# fibonacci(1.5) ??

def fibonacci(n):
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def is_int(n, is_pos=False):
    try:
        n = int(n)
        if is_pos:
            if n > 0:
                return True
            else:
                return False
        else:
            return True
    except:
        return False

if __name__ == '__main__':
    n = input("Enter the value of n:")
    if is_int(n, is_pos=True):
        n = int(n)
        for i in range(n):
            print(fibonacci(i))
        # print(fibonacci(n))
    else:
        print("Please enter a positive integer only.")
