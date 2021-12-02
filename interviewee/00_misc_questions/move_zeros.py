# write a function to move all the '0' elements
# within a list to the end while maintaining the 
# order of occourance for remaining elements
# Example: [0, 1, 0, 3, 12] --> [1, 3, 12, 0, 0]

# Given a list/array, move all the zeros within the array to the end maintaining the relative order of the other elements.

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
