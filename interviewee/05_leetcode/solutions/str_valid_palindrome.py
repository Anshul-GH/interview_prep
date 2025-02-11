'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ''.join(ch.lower() for ch in s if ch.isalnum())
        s_rev = s_clean[::-1]
        if s_rev == s_clean:
            return True
        else:
            return False
