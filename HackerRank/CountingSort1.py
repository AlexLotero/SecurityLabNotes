#!/bin/python3
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    freq_arr = [0] * 100
    result = []
    for i in arr:
        freq_arr[i] = freq_arr[i] + 1
    return freq_arr

    # THE SORTING STEP THAT IT ACTUALLY WASN'T ASKING ME TO MAKE...
    # last = 0
    # for j in freq_arr:
    #     if j != 0:
    #         last += 1
    #         for m in range(j):
    #             result.append(freq_arr.index(j, last))
    # return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
