# Write a function that accepts a positive integer and adds up all 
# the numbers starting from 1 to the number passed using recursion.
# Example:
# n=4 => 1+2+3+4 = 10
# n=7 => 1+2+3+4+5+6+7 = 28

# Step1: Recursive Case
# recursive_sum(n) = n + recursive_sum(n-1)

# Step2: Base Case
# recursive_sum(0) = 0

# Step3: Edge Cases or Constraints
# Only positive integers
# fibonacci(-1) ??
# fibonacci(1.5) ??

def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n-1)

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

if __name__ == "__main__":
    n = input('Enter the range upto which the sume should be calculated:')
    if is_int(n, is_pos=True):
        n = int(n)
        print(recursive_sum(n))
    else:
        print("Please enter a valid positive integer.")
