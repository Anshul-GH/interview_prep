'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.

'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''
        min_len = min([len(txt) for txt in strs])

        for i in range(min_len):    
            result = all(txt[:i+1] == strs[0][:i+1] for txt in strs)
            if result:
                lcp = strs[0][:i+1]
            else:
                break
                
        return lcp
