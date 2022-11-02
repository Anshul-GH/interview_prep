# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sstr = []

        ss_len = 0
        for chr in s:            
            if chr not in sstr:
                sstr.append(chr)
                if ss_len < len(sstr):
                    ss_len = len(sstr)
            elif len(sstr) > ss_len:
                ss_len = len(sstr)
                # find the index of the duplicate char
                idx = sstr.index(chr)
                if idx < len(sstr):
                    sstr = sstr[idx+1:]
                    sstr.append(chr)
                else:
                    sstr = []

        if ss_len == 0:
            ss_len = len(sstr)

        return ss_len
