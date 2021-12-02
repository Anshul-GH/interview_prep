# Question: Write a code to rotate a square matrix
"""
1 2 3         3 6 9
4 5 6  ---->  2 5 8
7 8 9         1 4 7
"""

# def rotate_matrix(arr):
#     # swap the corners
#     last=len(arr[0])
#     # tmp = arr[0][0]
#     # arr[0][0] = arr[0][len]
#     # arr[0][len] = tmp

#     for i in range(last):
#         for j in range(last):
#             tmp = arr[i,j]
#             arr[i,j] = a
#             arr[i+1,j] = arr[i,j]

import numpy as np

my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array)

def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer -1
        for i in range(first, last):
            # save top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # move bottom element to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # move right element to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move to right
            matrix[i][-layer-1] = top
    
    return matrix

print(rotate_matrix(my_array))
