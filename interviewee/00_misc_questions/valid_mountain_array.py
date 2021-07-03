# Given an array of integers arr, return true if and only if
# it is a valid mountain array. 
# Arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Example:
# Mountain Array: [0, 2, 3, 4, 5, 2, 1, 0]
# Not Mountain Array: [0, 2, 3, 3, 5, 2, 1, 0]


