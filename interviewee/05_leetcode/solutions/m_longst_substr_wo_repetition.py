# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_num = [ord(val) for val in s]

        prev_max = 0
        max = 0
        log = []
        for num in s_num:
            if num not in log:
                max += 1
                log.append(num)
                if prev_max < max:
                    prev_max = max
            else:
                if prev_max < max:
                    prev_max = max
                idx = log.index(num)
                if idx+1 != len(log):
                    log = log[idx+1:]
                else:
                    log = []
                log.append(num)
                max = len(log)

        return prev_max
        # sstr = []

        # ss_len = 0
        # for chr in s:            
        #     if chr not in sstr:
        #         sstr.append(chr)
        #         if ss_len < len(sstr):
        #             ss_len = len(sstr)
        #     elif len(sstr) > ss_len:
        #         ss_len = len(sstr)
        #         # find the index of the duplicate char
        #         idx = sstr.index(chr)
        #         if idx < len(sstr):
        #             sstr = sstr[idx+1:]
        #             sstr.append(chr)
        #         else:
        #             sstr = []

        # if ss_len == 0:
        #     ss_len = len(sstr)

        # return ss_len

