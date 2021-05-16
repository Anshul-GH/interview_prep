# Write a function that accepts a number and adds up all 
# the numbers from zero to the number passed to the function

def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n-1)

if __name__ == '__main__':
    range_n = int(input('Enter the range:'))
    
    print(recursive_sum(range_n))
