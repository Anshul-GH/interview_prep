# https://www.hackerrank.com/challenges/new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3


import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    breakpoint()
    ideal = list(range(1, len(q)+1))

    minm_bribe = 0

    for elem1, elem2 in zip(q, ideal):
        diff = elem1-elem2
        if diff > 2:
            minm_bribe = "Too chaotic"
            break
        elif diff > 0:
            minm_bribe += diff

    print(minm_bribe)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

# 1 2 5 3 7 8 6 4
# 1 2 3 4 5 6 7 8
# 0 0 2 -1 2 2 -1 -4

1 2 5 3 4 6 7 8
1 2 5 3 4 7 6 8
1 2 5 3 4 7 8 6