def fibonacci(n):
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def is_pos_int(n):
    try:
        n = int(n)
        if n > 0:
            return True
    except:
        return False

if __name__ == '__main__':
    n = input('Enter the value of n:')

    if is_pos_int(n):
        print(fibonacci(int(n)))
    else:
        print("Please enter a positive integer only.")
