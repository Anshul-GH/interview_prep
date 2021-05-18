# Write a function that accepts a number and adds up all 
# the numbers from zero to the number passed to the function

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


if __name__ == '__main__':
    range_n = input('Enter the range:')
    
    if is_int(range_n, is_pos=True):
        n = int(range_n)
        print(recursive_sum(n))
    else:
        print("Please enter a positive integer only.")
