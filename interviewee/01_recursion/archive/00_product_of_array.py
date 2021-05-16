# Write a function which takes an array of numbers as input and returns the product of them all
# Example: 
# product_of_array([1,2,3]) => 6
# product_of_array([1,2,3,4]) => 24

def product_of_array(arr):
    arr_len = len(arr)
    if arr_len == 0:
        return 1
    else:
        return arr[0] * product_of_array(arr[1:])

if __name__ == '__main__':
    arr_len = int(input('Input the length of array:'))
    arr = [0]*arr_len
    for i in range(arr_len):
        arr[i] = int(input(f"Enter element#{i}:"))

    print(product_of_array(arr))
