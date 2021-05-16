# code to calculate the factorial of a number

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

if __name__ == '__main__':
    num = input('Enter the number:')

    if is_int(num, is_pos=True):
        num = int(num)
        print(factorial(num))
    else:
        print("Please enter a positive integer only.")
