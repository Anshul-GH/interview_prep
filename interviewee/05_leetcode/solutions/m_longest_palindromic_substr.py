class Solution:
    def longestPalindrome(self, s: str) -> str:    
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # For each substring s[i...j], check if it is a palindrome. If it is,
        # then update the value of dp[i][j] to be the length of the palindrome.
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1] != 0):
                    dp[i][j] = j - i + 1

        # Return the longest palindromic substring by finding the maximum value
        # in the array dp and then extracting the substring from s.
        maxLength = 0
        start = 0
        end = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j] > maxLength:
                    maxLength = dp[i][j]
                    start = i
                    end = j

        return s[start:end + 1]

    # def check_palindrome(self, lst):    
    #     while lst:
    #         start = lst[0]
    #         end = lst[-1]
    #         if start == end:
    #             lst = lst[start+1:end]
    #             is_palindrome = True
    #         else:
    #             is_palindrome = False
    #             break
    #     else:
    #         # blank list
    #         is_palindrome = True
        
    #     return is_palindrome

    # def longestPalindrome(self, s: str) -> str:
    #     is_palindrome = False
    #     if len(s) == 1:
    #         is_palindrome = True
    #         sublst = s
    #     else:
    #         sublst = []
    #         s_num = [ord(val) for val in s]
    #         for num in s_num:
    #             start = s_num.index(num)
    #             rem_nums = s_num[start+1:]
    #             if num in rem_nums:
    #                 end = rem_nums.index(num)+start+2
    #                 sublst = s_num[start:end]
    #                 is_palindrome = self.check_palindrome(sublst)

    #     if is_palindrome and len(s) > 1:
    #         sublst = [chr(val) for val in sublst]
    #         sublst = "".join(sublst)
    #     elif not is_palindrome and s:
    #         sublst = s[0]            
        
    #     return sublst