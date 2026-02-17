# Given an array of integers nums and a target,
# return indices of two numbers that add up to target. 
# Assume exactly one solution exists,
# and you can't reuse the same element.

def twoSum(nums, target):
    seen = {}  # num: index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            print(seen)
            return [seen[complement], i]
        seen[num] = i    # Store after check (avoid self-match)
    print(seen)
    return []  # No solution

# Test
nums = [9, 2, 5, 7, 11, 15]
target = 10
print(twoSum(nums, target))
