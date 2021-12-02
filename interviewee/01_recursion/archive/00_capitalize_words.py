# Given an array of strings, write a function to 
# capitalize each string in the array.

def capitalize_word(arr):
    result = []
    if len(arr) == 0:
        return result
    
    result.append(arr[0].upper())
    return result + capitalize_word(arr[1:])

if __name__ == '__main__':
    arr_len = int(input('Input the length of array:'))
    arr = [0]*arr_len
    for i in range(arr_len):
        arr[i] = input(f"Enter string#{i}:")

    print(f'Original Array: {arr}')
    print(f"Cap'lzed Array: {capitalize_word(arr)}")
