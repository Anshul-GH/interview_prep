# Question: Find an element in a numpy array

import numpy as np

def find_element(arr, elem):

    for i in range(len(arr)):
        if arr[i] == elem:
            return i

my_array = np.array([1,2,3,4,5,6,7,8,9])
print(find_element(my_array, 6))
print(find_element(my_array, 11))
