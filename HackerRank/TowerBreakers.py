#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):            # writing out all of the small test cases (n = 0-5, m = 0-5) reveals the pattern
    # Write your code here          # didn't have to write complicated code, just had to solve for some to find the pattern
    if m == 1:
        return 2
    elif n % 2 == 0 and m > 1:
        return 2
    elif n % 2 == 1 and m > 1:
        return 1
    return 1
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()









# My alternative, way overly complicated code:
def towerBreakers(n, m):
    # Write your code here
    game_state = [m] * n
    x = 1
    game_fin = False
    turn_fin = False
    while True:
        for i in game_state:
            for j in range(2, math.ceil(i/2)):
                if i % j == 0:
                    i = i - j
                    x+=1
                    turn_fin = True
                    continue
                elif i > 1:
                    i = 1
                    x+=1
                    continue
                else:
                    
                    turn_fin = True
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()