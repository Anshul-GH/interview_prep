def my_decorator(func):
    '''Decorator Function'''
    def wrapper():
        '''Returns string F-I-B-O-N-A-C-C-I'''
        return 'F-I-B-O-N-A-C-C-I'
    return wrapper

@my_decorator
# equivalent to:
# pfib = my_decorator(pfib)
def pfib():
    '''Return Fibonacci'''
    return 'fibonacci'


print(pfib())
print(pfib)
