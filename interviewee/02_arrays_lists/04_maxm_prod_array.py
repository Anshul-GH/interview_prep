# Question: Find the maximum product of two integers in an array 
# All elements are positive integers. Array is numpy array

import numpy as np

arr = np.array([1, 20, 30, 44, 5, 65, 56, 57, 9, 8, 10, 31, 12, 13, 14, 35, 16, 27, 91, 19, 24])

# Solution1: using built-in sort function
srt_arr = np.sort(arr, )
max_prod = srt_arr[-1] * srt_arr[-2]

print(max_prod)

# Solution2: without sort function
def find_max_prod(arr):
    max_prod = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            prod = arr[i] * arr[j]
            if prod > max_prod:
                max_prod = prod
                pair = str(arr[i]) + ', ' + str(arr[j])

    print(pair)
    print(max_prod)

find_max_prod(arr)
