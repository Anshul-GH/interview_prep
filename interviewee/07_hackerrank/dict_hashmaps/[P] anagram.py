# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def check_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


def sherlockAndAnagrams(s):
    # breakpoint()
    # Write your code here
    # convert to list
    lst_s = list(s)
    set_s = list(set(lst_s))

    anagram_count = 0

    # the letters which are repeating will provide anagrams
    # anagram_count += (len(lst_s)-len(set_s))

    length = 1
    while length < len(s):
        s1 = s[0:length]
        for i in range(len(s)-length):
            # breakpoint()
            s2 = s[i+1:i+1+length]
            if check_anagram(s1, s2):
                anagram_count += 1
                print(anagram_count, s1, s2)
        length += 1

    return anagram_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        # fptr.write(str(result) + '\n')
        print(result)

    # fptr.close()
