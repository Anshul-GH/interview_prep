# calculate the power of n to an integer i --> (i)^n

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

def power(i, n):
    if n == 1:
        return i
    else:
        return i * power(i, n-1)

if __name__ == '__main__':
    i = input('Enter the integer i:')
    n = input('Enter the power n:')

    if is_int(i) and is_int(n):
        i = int(i)
        n = int(n)
        print(power(i, n))