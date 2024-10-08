'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rev = digits[::-1]
        int_num = 0
        dec = 0
        for num in rev:
            int_num += num * (10**dec)
            dec += 1
        
        # increment the number by 1
        int_num += 1

        # convert number into a list
        new_digits = str(int_num)
        new_digits = [int(digit) for digit in new_digits]
        
        return new_digits
