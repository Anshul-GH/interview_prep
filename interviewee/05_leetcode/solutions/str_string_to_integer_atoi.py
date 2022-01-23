'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.

Note:

    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

'''

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        int_range = (-2**31, 2**31 -1)    
        number = '0'

        count = 0
        if len(s) > 0:
            while count < len(s):
                if ord(s[count]) == 45 and len(s) > 1 and s[count+1].isdigit():
                    number = '-'
                    count += 1
                elif ord(s[count]) == 43 and len(s) > 1 and s[count+1].isdigit():
                    count += 1
                elif 48 <= ord(s[count]) <= 57:
                    if number == '0':
                        number = s[count]
                    else:
                        number += s[count]
                    count += 1
                    while count < len(s) and 48 <= ord(s[count]) <= 57:
                        number += s[count]
                        count += 1
                    break
                else:
                    # count += 1
                    break

        number = int(number)
        if int(number) < int_range[0]:
            number = int_range[0]
        elif int(number) > int_range[-1]:
            number = int_range[-1]

        return number
