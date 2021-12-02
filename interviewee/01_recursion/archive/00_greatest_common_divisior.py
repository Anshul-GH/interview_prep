### Step-1: Recursive Case ###
# GCD - Laregst positive integer that divides the numbers without a remainder

# GCD(8, 12) == 4
# 8 = 2*2*2
# 12 = 2*2*3
# GCD = 2*2 = 4

# Euclidean Algorithm (Recursion)
# GCD(48, 18)
# - 48/18 = 2 remainder 12
# - 18/12 = 1 remainder 6
# - 12/6 = 2 remainder 0
# => GCD(48,18) = 6

# Condition
# GCD(a, 0) = 0 and GCD(a, b) = GCD(b, (a%b))

### Step-2: Base Condition ###
# if b == 0
# GCD(a, 0) = 0

### Step-3: Unintentional Cases ###
# Positive integers only

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

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, (a%b))

if __name__ == '__main__':
    a = input('Enter a:')
    b = input('Enter b:')

    if is_int(a, is_pos=True) and is_int(b, is_pos=True):
        a = int(a)
        b = int(b)
        print(gcd(a, b))
    else:
        print("Please enter positive integers only for a and b.")
