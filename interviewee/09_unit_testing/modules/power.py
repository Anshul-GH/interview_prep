from typing import Type


def power_num(number: float, power: int) -> float:
    '''
    Raise the number to the power if number >= 0
    '''
    # the number can be int or float
    if not isinstance(number, int) and not isinstance(number, float):
        raise TypeError('The number can only be int or float.')
    # the power can only be int
    if not isinstance(power, int):
        raise TypeError('The power can only be of type int.')

    # perform the calculation only if the number is positive
    if number >= 0:
        return round(number ** power, 2)
    else:
        raise TypeError('Number can only be >= 0.')
