# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    i = 0
    while (i < len(arr)):
        # current element is not at its right position
        if (arr[i] != i+1):
            while (arr[i] != i+1):
                # swap the current element with the one
                # at the correct position of that element
                temp = 0
                temp = arr[arr[i] - 1]
                arr[arr[i] - 1] = arr[i]
                arr[i] = temp

                count += 1

        # once the current element is at the right position, move on
        i += 1

    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    # fptr.write(str(res) + '\n')

    # fptr.close()
    print(res)
