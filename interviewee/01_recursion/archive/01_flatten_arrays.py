# Write a function which accepts an array of arrays
# and returns a new array with all values flattened.

# Examples:
# flatten([1,2,3,[4,5]]) => [1,2,3,4,5]
# flatten([1,[2,[3,4],[[5]]]]) => [1,2,3,4,5]
# flatten([[1],[2],[3]]) => [1,2,3]

def flatten(arr):
    result = []
    for val in arr:
        if isinstance(val, int):
            result.append(val)
        else:
            result.extend(flatten(val))
    
    return result

if __name__ == '__main__':
    print(flatten([1,2,3,[4,5]]))
    print(flatten([1,[2,[3,4],[[5]]]]))
    print(flatten([[1],[2],[3]]))
