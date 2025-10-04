#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):                                 # Sliding window implementation
    # Write your code here
    arr.sort()
    current_min = 9999999999999999999999999999999   # Just has to be higher than any test case's minimum unfairness
    current_L = 0
    current_R = k
    while current_R <= len(arr):
        # temp_arr = arr[current_L:current_R]       # Slicing every iteration added compute time, for O(n * k) down to O(n)
        # print(temp_arr)
        temp_unfair = arr[current_R-1] - arr[current_L]
        if temp_unfair < current_min:
            current_min = temp_unfair
        current_L += 1
        current_R += 1
    # print(current_min)
    return current_min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

















import math
# arr = [1, 4, 7, 2]
# k = 2
# arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
# k = 4
# arr = [4504, 1520, 5857, 4094, 4157, 3902, 822, 6643, 2422, 7288, 8245, 9948, 2822, 1784, 7802, 3142, 9739, 5629, 5413, 7232]
# k = 5
arr = [1, 2, 1, 2, 1]
k = 2
arr.sort()
print(arr)
# # arr_1 = arr[-(k-1):]
# # arr_1.append(min(arr))
# arr_1 = arr[:k]
# print(arr_1)
# print(max(arr_1) - min(arr_1))
cur_min = max(arr)
for i in arr:
    for j in arr:
        if i > j and (i - j) < cur_min and (i - j) >= 0 and (abs(arr.index(i) - arr.index(j))) > (k-2):
            cur_min = i - j
            print(i, j)
            print(arr.index(i), arr.index(j))

print(cur_min)


# have to find fix for when the values of i and j are the same (but they are 'different' elements)



#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr.sort()
    cur_min = max(arr)
    for i in arr:
        for j in arr:
            if i > j and (i - j) < cur_min and (i - j) > 0 and (abs(arr.index(i) - arr.index(j))) > (k-2):
                cur_min = i - j
    return cur_min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

