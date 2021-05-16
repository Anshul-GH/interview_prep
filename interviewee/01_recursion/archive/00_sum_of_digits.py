# find the sum of digits of a positive number using recursion

# Step-1: Recursive Case - the flow

# 54 --> 54/10 = 5 and remainder = 4
# 10 --> 10/10 = 1 and remainder = 0
# 112 --> 112/10 = 11 and remainder = 2
#           11/10 = 1 and remainder = 1

# f(n) = n%10 + f(n/10)

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


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)


if __name__ == '__main__':
    n = input('Enter the positive integer number:')

    # proceed only if the number entered is a positive integer
    if is_int(n, is_pos=True):
        n = int(n)
        print(sum_of_digits(n))
    else:
        print('Please enter a positive integer only.')
