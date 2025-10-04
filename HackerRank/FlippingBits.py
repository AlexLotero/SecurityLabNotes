#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    result = ''
    final_result = 0
    binary = bin(n)[2:]
    while len(binary) < 32:
        binary = '0' + binary
    for i in binary:
        if i == '1':
            result += '0'
        elif i == '0':
            result += '1'
    # for c in range(len(result)):
    #     if result[c] == 1:
    #         final_result += 2^c
    # return final_result
    return int(result, 2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()