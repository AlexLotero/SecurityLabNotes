#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        return -1
    
    lhs = int(len(s)/ 2)
    fr_half = s[:lhs]                                                        # more slicing, try to acoid
    bk_half = s[lhs:]

    fr_count = Counter(fr_half)
    bk_count = Counter(bk_half)

    # in_common = set(fr_half.intersection(set(bk_count.lower())))          # couldn't use this, it removed the duplicates that I actually needed

    in_common = []
    for char in fr_count.keys() & bk_count.keys():                          # Get common characters
        in_common.extend([char] * min(fr_count[char], bk_count[char]))      # Keep duplicates# set(fr_half) & set(bk_half)

    # common_nodup = list(set(in_common))

    ct_common = len(in_common)
    if ct_common == 0:                                                      # if they have no letters in common, we must swap all of them to get an anagram
        # print(len(fr_half))
        return len(fr_half)
    if "".join(sorted(fr_half)) == "".join(sorted(bk_half)):                # if they're already equal, we already have an anagram
        # print(0)
        return 0
    # print("".join(sorted(fr_half)), "".join(sorted(bk_half)))

    for i in in_common:                                                     # replace only one occurence of each shared character, that way if only one string had more of a certain letter,
        fr_half = fr_half.replace(i, "", 1)                                 # that nuance is preserved
        bk_half = bk_half.replace(i, "", 1)

    # print(fr_half, bk_half)
    return(max(len(fr_half), len(bk_half)))                                 # whichever string had more 'unique' characters from the other contains the minimum number of swaps to match
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
