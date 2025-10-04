#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):                               # mostly just reading directions carefully - logic was easy enough to understand
    # Write your code here
    # print(queries)                                        # large prints were causing HackerRank test cases to report wrong answers - BE CAREFUL
    arr = [[] for _ in range(n)]                            # THIS is what is meant by "declare a 2-dimensional array, arr, of n empty arrays"
    # print(arr, type(arr))
    answers = []
    lastAnswer = 0
    for i in queries:
        if i[0] == 1:
            idx = ((i[1] ^ lastAnswer) % n)
            arr[idx].append(i[2])
        else:
            idx = ((i[1] ^ lastAnswer) % n)
            # print('idx: ', idx)
            # print('arr: ', arr)
            lastAnswer = arr[idx][i[2] % len(arr[idx])]
            answers.append(lastAnswer)
        # print('arr: ', arr)                               # large prints were causing HackerRank test cases to report wrong answers - BE CAREFUL
        # print('answers: ', answers)                       # large prints were causing HackerRank test cases to report wrong answers - BE CAREFUL
    return answers
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
