#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    # n = len(A)
    # perm_A = list(itertools.permutations(A))
    # perm_B = list(itertools.permutations(B))
    # # print(perm_A, perm_B)
    # check = []
    # for i in perm_A:
    #     temp_check = True
    #     for j in perm_B:
    #         # print(i, j)
    #         for m in range(len(i)):
    #             # print(m)
    #             if i[m] + j[m] < k:
    #                 temp_check = False
    #             # print(temp_check)
    #         if temp_check:
    #             check.append(1)
    #         else:
    #             check.append(0)
    
    A.sort()
    B.sort(reverse="True")
    check = True
    for i in range(len(A)):
        if A[i] + B[i] < k:
            check = False
            
    if check:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
