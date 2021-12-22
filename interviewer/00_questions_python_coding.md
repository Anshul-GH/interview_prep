## Programming - Basic


```python
# Given a list:
lst = [1,2,3,4,6,7,8,9,12,4,2,5,7,2,5,2,1,4,6,3]
# Push all the even numbers to the front and odd numbers to the back
# Expected Output (one possibility):
output = [6,8,4,2,4,2,12,2,4,2,6,7,1,5,3,9,7,3,5,1]
# Note:
# 1. The order of occourance of the numbers can change
# 2. Do not use any temporary variables.
```


```python
# Test the solution:
lst = [1,2,3,4,6,7,8,9,12,4,2,5,7,2,5,2,1,4,6,3]
sorted(lst, key=lambda x:x % 2)
```




    [2, 4, 6, 8, 12, 4, 2, 2, 2, 4, 6, 1, 3, 7, 9, 5, 7, 5, 1, 3]



----------------------------------------------------------------


```python
# Given a list:
lst = [0,2,1,3,5,5,6,8,7,9]
# Print all the values where index == value
# Output:
output = [0, 3, 5, 6, 9]

```


```python
# Test the solution:
lst = [0,2,1,3,5,5,6,8,7,9]
[idx for idx, val in enumerate(lst) if idx==val]
```




    [0, 3, 5, 6, 9]




```python
lst = [0,2,1,3,5,5,6,8,7,9]

for i in range(len(lst)):
    if i==lst[i]:
        print(i)
```

    0
    3
    5
    6
    9


----------------------------------------------------------------


```python
# Given a list:
lst = [0, 1, 0, 3, 12, 0, 6, 4, 0, 5, 9, 0, 2, 3, 0]
# Push all the zeros to the back
# Expected Output:
output = [1, 3, 12, 6, 4, 5, 9, 2, 3, 0, 0, 0, 0, 0, 0]
# Note:
# 1. The order of occourance of the numbers can change
# 2. Do not use any temporary variables
```


```python
# Test the solution:
lst = [0, 1, 0, 3, 12, 0, 6, 4, 0, 5, 9, 0, 2, 3, 0]
sorted(lst, key=lambda x: x == 0)
```




    [1, 3, 12, 6, 4, 5, 9, 2, 3, 0, 0, 0, 0, 0, 0]



----------------------------------------------------------------

## Programming - Intermediate/Advanced


```python
# Given an array, rotate the array to the right by k steps, where k is non-negative.
# k can be any finite integer value.
# Input: 
nums = [1,2,3,4,5,6,7]
k = 3
# Output: 
[5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
```


```python
# Test the solution:
def rotate_array_by_k(elements,k):
    rotate_by = k % len(elements)
    return elements[:-rotate_by] + elements[rotate_by:-rotate_by]
```

----------------------------------------------------------------


```python
# Write a code to merge two lists iteratively in such a way that:
# * For each iteration, one element will be picked up from each list and added to the output list
# * After each iteration, the result in the output list should always be sorted
# The lists can be of different lengths so if one gets exhausted, continue the iteration with the remaining elements of the other list
# Example:
# Iteration1: [11,90]
# Iteration2: [4,11,55,90]
# Iteration3: [4,11,55,66,88,90]
# Iteration4: [4,11,33,55,66,66,88,90]
# Iteration5: [4,11,22,33,55,66,66,88,90]
# Iteration6: [4,11,22,33,55,66,66,88,90,99]
list1 = [11, 4, 88, 66]
list2 = [90, 55, 66, 33, 22, 99]
```


```python
# Test the solution:
list1 = [11, 4, 88, 66]
list2 = [90, 55, 66, 33, 22, 99]

res = []

length = [len(list1), len(list2)]
length = sorted(length)

l1_len = len(list1)
l2_len = len(list2)

for i in range(length[-1]):
    if i < l1_len:
        a = list1[i]
        res.append(a)
    
    if i < l2_len:
        b = list2[i]
        res.append(b)
        
    res = sorted(res)
    print(res)
```

----------------------------------------------------------------


```python
# Fibonacci series using generators
```


```python
# Test the solution:
def fib():
    a,b = 0,1
    while True:
        yield a
        b = a+b
        yield b
        a = a+b
```


```python
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Example 3:
# Input: strs = ["vet","veteran","vetter"]
# Output: "vet"

# Example 4:
# Input: strs = ["apple","crapple","grapple"]
# Output: ""

# Constraints:
#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lower-case English letters.
```


```python
# Test the solution
def longestCommonPrefix(strs):
    lcp = ''
    min_len = min([len(txt) for txt in strs])

    for i in range(min_len):    
        result = all(txt[:i+1] == strs[0][:i+1] for txt in strs)
        if result:
            lcp = strs[0][:i+1]
        else:
            break
            
    return lcp
```

-----------------------------


```python
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Example 4:
# Input: x = 0
# Output: 0

# Constraints: -2^31 <= x <= 2^31 - 1
```


```python
# Test the solution:
def reverse(self, x: int) -> int:
    neg = False
    if x < 0:
        neg = True
    x_rev = list(str(abs(x)))
    x_rev.reverse()
    x_rev = int(''.join(x_rev))

    if abs(x_rev) > (2**31 - 1):
        return 0
    elif neg:
        x_rev = x_rev*-1
        return x_rev
    else:
        return x_rev
```

-----------
