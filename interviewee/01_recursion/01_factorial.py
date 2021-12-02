# Factorial: Product of all positive integers, less than or equal to n.
# Works only with positive integers
# 0! = 1

# Step1: Recursive Case
# n! = n * (n-1)!

# Step2: Base Case
# 0! = 1
# 1! = 1

# Step3: Edge Cases or Constraints
# Only positive integers
# factorial(-1) ??
# factorial(1.5) ??

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

def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    num = input("Enter the number for which factorial needs to be calculated:")

    if is_int(num, is_pos=True):
        num = int(num)
        print(factorial(num))
    else:
        print("Please enter a positive integer only.")
