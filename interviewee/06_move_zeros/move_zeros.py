def move_zeros(arr):
    # non_zero_counter
    counter = 0
    for val in arr:
        if val != 0:
            arr[counter] = val
            counter += 1

    remaining = len(arr) - counter
    arr[counter:] = [0]*remaining

    return arr


if __name__ == '__main__':
    arr = [0, 2, 0, 1, 4]
    print(arr)
    arr_mod = move_zeros(arr)
    print(arr_mod)
