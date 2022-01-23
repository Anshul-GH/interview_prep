'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        found = False
        if len(needle) == 0:
            found = True
            index = 0
        else:
            length = len(needle)
            index = 0        
            while (index + length <= len(haystack)):
                if haystack[index:index + length] == needle:
                    found = True
                    break
                else:
                    index += 1

        if not found:
            index = -1

        return index
