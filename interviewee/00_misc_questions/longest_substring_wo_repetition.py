# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0

### unsolved ###
def find_longest_non_repeating_substr(strg):
    str_lst = list(strg)
    track_chr = {}
    max_len = 0
    
    for idx, val in enumerate(str_lst):
        if val in track_chr:
            track_chr[val] = idx
        else:
            max_len += 1



if __name__ == '__main__':
    pass
