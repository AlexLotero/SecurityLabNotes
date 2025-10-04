#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    up_alpha = string.ascii_uppercase
    low_alpha = string.ascii_lowercase
    
    wrap_num = k % len(low_alpha)
    rot_alpha = low_alpha[wrap_num:] + low_alpha[:wrap_num]
    
    enc = ''
    for i in s:
        if i in up_alpha:
            # s = s.replace(i, rot_alpha[up_alpha.index(i)].upper())
            enc += rot_alpha[up_alpha.index(i)].upper()
        elif i in low_alpha:
            # s = s.replace(i, rot_alpha[low_alpha.index(i)])
            enc += rot_alpha[low_alpha.index(i)]
        else:
            enc += i
    return enc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()