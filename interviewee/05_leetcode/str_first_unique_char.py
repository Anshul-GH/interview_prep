'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

 

Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.

'''

class Solution:    
    def firstUniqChar(self, s: str) -> int:
        def get_unique(arr):
            uniq_lst = []
            n = len(arr)
            if arr[0] != arr[1]:
                uniq_lst.append(arr[0])

            # Check for all the elements
            # if it is different its
            # adjacent elements
            for i in range(1, n - 1):
                if (arr[i] != arr[i + 1] and
                    arr[i] != arr[i - 1]):
                    uniq_lst.append(arr[i])

            # Check for the last element
            if arr[n - 2] != arr[n - 1]:
                uniq_lst.append(arr[n-1])

            return uniq_lst

        if len(s) > 1:
            s_list = list(s)
            s_copy = s_list.copy()
            s_copy.sort()

            s_uniq = get_unique(s_copy)

            pos = -1
            for idx, val in enumerate(s_list):
                if val in s_uniq:
                    pos = idx
                    break
        elif len(s) == 1:
            pos = 0
        else:
            pos = -1
        return pos
