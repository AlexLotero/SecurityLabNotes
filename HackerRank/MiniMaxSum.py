#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_sum, max_sum = 0, 0
    
    arr_min = arr[:]
    arr_max = arr[:]
    
    arr_min.remove(max(arr))
    arr_max.remove(min(arr))
    
    min_sum = sum(arr_min)
    max_sum = sum(arr_max)
    
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
