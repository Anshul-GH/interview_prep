def square_preceding(value):
    '''
    Replace each item in the list with square of the value
    preceding the item and replace the first item with zero.

    Example:
    lst1 = [1, 2, 3]
    square_preceding(lst1)
    lst1 = [0, 1, 4] 
    '''

    if value:
        for i in range(len(value)):
            value[i] = round(value[i] ** 2, 2)

        value[1:] = value[:-1]
        value[0] = 0
        
    return value
