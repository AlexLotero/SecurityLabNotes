#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    pairs = 0
    i = 0
    while i < len(ar):              # while loop to fine tune edits to the iterator(1) 
        try:
            if ar[i] == ar[i+1]:
                pairs += 1
                i += 2              # NOTICE THE DIFFERENCE, how we update the iterator
            elif ar[i+1] == ar[i+2]:
                pairs += 1
                i += 3              # NOTICE THE DIFFERENCE, how we update the iterator
            else:
                i += 2              # NOTICE THE DIFFERENCE, how we update the iterator
        except Exception:
            i += 2
            pass
    return pairs
    # (1) "Changing the value of i directly within a for loop won't affect the loop's behavior. The loop will continue to iterate based on the original sequence."

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
