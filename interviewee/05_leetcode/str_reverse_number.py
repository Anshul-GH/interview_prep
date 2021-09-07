'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-2^31 <= x <= 2^31 - 1
'''


class Solution:
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
