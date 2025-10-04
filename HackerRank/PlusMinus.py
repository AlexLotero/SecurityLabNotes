#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos, neg, zero = 0, 0, 0
    n = len(arr)
    for i in arr:
        #print(pos, neg, zero)
        if i >= 1:
            pos = pos + 1
        elif i == 0:
            zero = zero + 1
        else:
            neg = neg + 1
    print(round((pos/n), 6))
    print(round((neg/n), 6))
    print(round((zero/n), 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
