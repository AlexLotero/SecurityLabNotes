#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):                                             # SUMMARY: must avoid slicing at all costs - it is constantly causing me to exceed execution time limits
    # Write your code here
    if s == s[::-1]:
        return -1
    mismatch = False
    # mismatch_loc = []
    mismatch_loc_1 = -6
    for char in range(int(len(s)/2)):
        # print(s[char], s[len(s) - char - 1])
        # exit()
        if s[char] != s[len(s) - char - 1]: # s[::-1][char]:        # <----------------------------------------
            mismatch = True
            # mismatch_loc.append(char)
            mismatch_loc_1 = char
            mismatch_loc_2 = len(s) - char - 1
            # print(mismatch, mismatch_loc_1, mismatch_loc_2, s)
            break
    if not mismatch:
        return -1
    if mismatch_loc_1 != -6:
        if mismatch_loc_1 == 0:
            temp_s_1 = s[1:]                                        # <------------------------------- somehow passed test cases
            temp_s_2 = s[:-1]
            # print(s, temp_s_1, temp_s_2)
        # elif mismatch_loc_1 == (len(s)-1):
        #     temp_s_1 = s[:len(s)-1]
        #     temp_s_2 = s[]
        else:
            temp_s_1 = s[:mismatch_loc_1] + s[mismatch_loc_1+1:]
            temp_s_2 = s[:mismatch_loc_2] + s[mismatch_loc_2+1:]
        if temp_s_1 == temp_s_1[::-1]:
            return mismatch_loc_1
        elif temp_s_2 == temp_s_2[::-1]:
            # print('Here: ', mismatch_loc_2)
            return mismatch_loc_2
    # for i in mismatch_loc:
    #     temp_s = s[:i] + s[i+1:]
    #     if temp_s == temp_s[::-1]:
    #         return i
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
