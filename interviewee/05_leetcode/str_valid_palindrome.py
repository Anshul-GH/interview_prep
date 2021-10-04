class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ''.join(ch.lower() for ch in s if ch.isalnum())
        s_rev = s_clean[::-1]
        if s_rev == s_clean:
            return True
        else:
            return False
