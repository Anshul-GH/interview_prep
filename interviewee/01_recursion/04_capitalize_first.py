# Given an array of strings, write a function to 
# capitalize the first letter of each string in the array.

def capitalize_first(arr):
    result = []
    if len(arr) == 0:
        return result
    else:
        result.append(arr[0].capitalize())
        return result + capitalize_first(arr[1:])

if __name__ == '__main__':
    arr_len = int(input('Input the length of the array:'))
    arr = [0] * arr_len

    for i in range(arr_len):
        arr[i] = input(f'Enter string #{i}:')
    
    print(f'Original Array: {arr}')
    print(f"Cap'lzed Array: {capitalize_first(arr)}")
