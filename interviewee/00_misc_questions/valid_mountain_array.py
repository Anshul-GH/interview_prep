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

# my solution
def check_mountain_array(arr):
    is_mountain_array = False
    
    counter = 0
    arr_len = len(arr)

    # minm length for mountain array == 3:
    if arr_len < 3:
        return False

    while counter < arr_len-1:
        if arr[counter] < arr[counter+1] and counter < arr_len-2:
            is_mountain_array = True
            counter += 1
        elif arr[counter] > arr[counter+1] and counter < arr_len-1:
            is_mountain_array = True    
            counter += 1
        else:
            is_mountain_array = False
            break

    return is_mountain_array


# smart solution
def check_mountain_array_smartly(arr):
    counter = 1
    arr_len = len(arr)

    # minm length for mountain array == 3:
    if arr_len < 3:
        return False

    while counter < arr_len and arr[counter-1] < arr[counter]:
        counter += 1
    if counter == 1 or counter == arr_len:
        return False
    while counter < arr_len and arr[counter-1] > arr[counter]:
        counter += 1

    return (counter == arr_len)


if __name__ == '__main__':
    # my_arr = [1, 2, 3, 1]
    my_arr = [0, 1]
    # [0, 2, 3, 3, 5, 2, 1, 0]
    # [0, 2, 3, 4, 5, 2, 1, 0]
    # [0, 2, 3, 4, 5, 2, 1]
    is_mountain_array = check_mountain_array(my_arr)
    is_mountain_array_smart = check_mountain_array_smartly(my_arr)
    print(is_mountain_array, is_mountain_array_smart)
