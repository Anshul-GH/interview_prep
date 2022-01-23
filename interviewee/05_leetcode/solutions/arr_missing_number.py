'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


Constraints:
    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    All the numbers of nums are unique.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sort the array
        nums.sort()
        len_nums = len(nums)

        idx = 0
        # first element (zero) is missing:
        if nums[idx] != 0:
            return idx
        
        while idx < len_nums-1:
            if nums[idx+1] - nums[idx] != 1:
                return (idx+1)
            elif nums[len_nums-idx-1] - nums[len_nums-idx-2] != 1:
                return (len_nums-idx-1)
            idx += 1

        # last element in the list is missing
        return len_nums

# alternate
        # nums.sort()
        # idx = 0    
        # while(idx < len(nums) and idx == nums[idx]):
        #     idx += 1
        #     continue

        # return idx