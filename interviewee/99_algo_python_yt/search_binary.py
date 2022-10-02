# iterative binary search
def iterative_binary_search(arr, start, end, target):
    while end >= start:
        mid = (start+end) // 2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid


# recursive binary search
def recursive_binary_search(arr, start, end, target):
    if end >= start:
        mid = (start+end) // 2

        if arr[mid] > target:
            recursive_binary_search(arr, mid+1, end, target)
        elif arr[mid] < target:
            recursive_binary_search(arr, start, mid-1, target)
        else:
            return mid
    else:
        return -1


def main():
    arr = [2, 5, 9, 1, 3, 22, 7, 16]
    target = 1

    print(recursive_binary_search(arr, 0, len(arr)-1, target))
    # print(iterative_binary_search(arr, 0, len(arr)-1, target))


if __name__ == "__main__":
    main()
