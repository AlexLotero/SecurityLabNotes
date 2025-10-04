#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    book = [1]
    i = 2
    while i <= (n):
        if i < (n):
            book.append([i, i+1])
            i+=2
        else:
            book.append(i)
            i+=2    
    # print(book)   

    first_half = book[:math.ceil(len(book)/2)]
    second_half = book[math.ceil(len(book)/2):]
    second_half.reverse()

    for x in range(len(first_half)):
        try:
            if first_half[x] == p or p in first_half[x]:
                return x
                # print("Shortest is x: ", x)
        except Exception:
            pass
    for y in range(len(second_half)):
        try:
            if second_half[y] == p or p in second_half[y]:
                return y
                # print("Shortest is y: ", y)
        except Exception:
            pass
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()