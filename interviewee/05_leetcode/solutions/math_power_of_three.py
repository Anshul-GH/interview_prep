'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true

Example 4:
Input: n = 45
Output: false

Constraints:
    -2^31 <= n <= 2^31 - 1

 
Follow up: Could you solve it without loops/recursion?
'''
class Solution:
    def check_multiple_of_three(self, n):
        flag = False
        while (n%3 == 0) and (n//3 != 1):        
            n = n//3
        if n == 3:
            flag = True

        return flag

    def isPowerOfThree(self, n: int) -> bool:
        # check even or n=0
        if abs(n) % 2 == 0 or n == 0:
            return False
        # exactly equal to 3 or 1
        elif n == 3 or n == 1:
            return True    
        else:
            return self.check_multiple_of_three(n)
