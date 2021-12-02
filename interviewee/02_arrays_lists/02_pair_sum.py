# Question: Given a list, find the index of pairs whose sum is equal to a given target
# Example:
# input_array = [2, 6, 3, 9, 11], target_num = 9
# Output: [1,2]

# Additional Information:
# list only contains positive integers
# if same pair repeats print all index combinations. 
# Example: input_array = [2, 6, 3, 10, 11, 3, 8, 4, 6], target_num = 9. Output: [1, 2], [1, 5], [2, 8]
# one pair of index should not repeat. 
# Example index pairs [1, 2] and [2, 1] should be treated as same

def find_pairs(lst, target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            # if lst[i] == lst[j]:
            #     # ignore
            #     continue
            # elif lst[i] + lst[j] == target:
            if lst[i] + lst[j] == target:
                print([i, j])

# if __name__ == "__main__":    
input_array = [1,2,3,2,3,4,5,6]
target = 6
find_pairs(input_array, target)
