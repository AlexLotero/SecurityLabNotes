#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    grid_sort = []
    for i in grid:
        x = ''.join(sorted(i))
        grid_sort.append(x)
        
    for k in range(len(grid_sort[0])):
        temp_list = []
        for j in range(len(grid_sort)):
            temp_list.append(grid_sort[j][k])
        temp_list_unsort = temp_list[:]
        temp_list.sort()
        if temp_list_unsort != temp_list:
            return 'NO'
            # print('NO')

    return 'YES'
    # print('YES')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()