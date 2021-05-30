# Question: Write a code to rotate a square matrix
"""
1 2 3         3 6 9
4 5 6  ---->  2 5 8
7 8 9         1 4 7
"""

def rotate_matrix(arr):
    # swap the corners
    last=len(arr[0])
    # tmp = arr[0][0]
    # arr[0][0] = arr[0][len]
    # arr[0][len] = tmp

    for i in range(last):
        for j in range(last):
            tmp = arr[i,j]
            arr[i,j] = a
            arr[i+1,j] = arr[i,j]



