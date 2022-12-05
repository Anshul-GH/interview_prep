class Solution:
    def check_palindrome(self, lst):    
        while lst:
            start = lst[0]
            end = lst[-1]
            if start == end:
                lst = lst[start+1:end]
                is_palindrome = True
            else:
                is_palindrome = False
                break
        else:
            # blank list
            is_palindrome = True
        
        return is_palindrome

    def longestPalindrome(self, s: str) -> str:
        is_palindrome = False
        if len(s) == 1:
            is_palindrome = True
            sublst = s
        else:
            sublst = []
            s_num = [ord(val) for val in s]
            for num in s_num:
                start = s_num.index(num)
                rem_nums = s_num[start+1:]
                if num in rem_nums:
                    end = rem_nums.index(num)+start+2
                    sublst = s_num[start:end]
                    is_palindrome = self.check_palindrome(sublst)

        if is_palindrome and len(s) > 1:
            sublst = [chr(val) for val in sublst]
            sublst = "".join(sublst)
        elif not is_palindrome and s:
            sublst = s[0]            
        
        return sublst