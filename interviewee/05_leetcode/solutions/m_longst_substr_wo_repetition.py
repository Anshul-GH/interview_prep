# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sstr = []

        ss_len = 0
        for chr in s:            
            if chr not in sstr:
                sstr.append(chr)
            elif len(sstr) > ss_len:
                ss_len = len(sstr)
                # find the index of the duplicate char
                idx = sstr.index(chr)
                sstr = sstr[1:]

        if ss_len == 0:
            ss_len = len(sstr)

        return ss_len
