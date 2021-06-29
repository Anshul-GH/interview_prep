def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


arr = [1, 2, 3, 4, 5, 6]
target = 1

result = binary_search(arr, target)

if result != -1:
    print('Element is present at index: ', result)
else:
    print('Element is not present in the list')
