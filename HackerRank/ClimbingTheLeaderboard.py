#!/bin/python3

import math
import os
import random
import re
import sys
import bisect                                           # https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    # approach it backwards? - prepend, do exactly what I am doing now, but backwards and prepend to new_rank
    unique = list(set(ranked))#[::-1]
    unique.sort()
    new_rank = []
    for i in player:
        # unique = [x for x in unique if x > i]
        index = bisect.bisect(unique, i)            # "This function returns the position in the sorted list (unique), where the number passed in argument "i" can be 
        count = (len(unique)) - index               # placed so as to maintain the resultant list in sorted order - utilizes binary search algorithm O(log n)""
        new_rank.append(count + 1)                  # https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
        # new_rank.insert(0, count)
        # print(index, len(unique), count, new_rank)
    return new_rank

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
