# https://leetcode.com/problems/sqrtx/
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return x
        else:
            root = 0
            for i in range((x//2)+1):
                square = i*i
                if square == x:
                    root = i
                    break
                elif square > x:
                    root = i - 1
                    break
            
            return root
