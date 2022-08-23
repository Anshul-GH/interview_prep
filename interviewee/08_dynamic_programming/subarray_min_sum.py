# Find the sub-array with minimum sum
# Example:
# lst = [20, -7, -3, 9, -4, 6, -9, 10]

from random import randint


def subarray_min_sum(arr):
    if len(arr) == 0:
        return 0
    
    min_sum = arr[0]
    min_sum_using_element = [arr[0]]

    for i in range(1, len(arr)):
        num = arr[i]
        current_min = min(num, num + min_sum_using_element[i-1])
        min_sum_using_element.append(current_min)
        min_sum = min(min_sum, current_min)
        # print(min_sum, min_sum_using_element)
    
    return min_sum

if __name__ == "__main__":
    # list of 100 elements
    lst = [randint(-9, 10) for _ in range(20)]
    print(subarray_min_sum(lst))
