# https://www.hackerrank.com/challenges/two-strings/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Given two strings, determine if they share a common substring. A substring may be as small as one character.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


def twoStrings(s1, s2):
    # Write your code here    
    lst_s1 = list(set(s1))
    lst_s2 = list(set(s2))
    lst_joint = list(set(lst_s1+lst_s2))

    len_orig = len(lst_s1) + len(lst_s2)
    len_joint = len(lst_joint)

    if len_orig == len_joint:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        # fptr.write(result + '\n')
        print(result)

    # fptr.close()
