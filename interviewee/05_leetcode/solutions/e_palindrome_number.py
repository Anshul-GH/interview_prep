# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst_x = list(str(x))
        revl_x = lst_x[::-1]

        if revl_x == lst_x:
            return True
        else:
            return False
