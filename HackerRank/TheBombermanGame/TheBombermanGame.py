#!/bin/python3

import math
import os
import random
import re
import sys
import copy

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    
    rows, cols = len(grid), len(grid[0])
    
    if n == 1:
        return grid
    if n % 2 == 0:
        foo = [['O' for _ in range(cols)] for _ in range(rows)]
        return ["".join(row) for row in foo]
    
    cert_state = n % 4
    if cert_state == 3:
        n = 3
    elif cert_state == 1:
        n = 5

    grid_list = [list(row) for row in grid]
    temp_grid = [['O' for _ in range(cols)] for _ in range(rows)]
    state = 2   # 1
    while state <= n:
        if state % 2 == 0:  # if n % 3 == 2:
            temp_grid = [['O' for _ in range(cols)] for _ in range(rows)]
            
        else: 
            for x in range(rows):
                for y in range(cols):
                    if grid_list[x][y] == 'O':
                        if grid_list[x][y] == 'O':
                            if x+1 < rows:
                                temp_grid[x+1][y] = '.'
                            if x-1 >= 0:
                                temp_grid[x-1][y] = '.'
                            if y+1 < cols:
                                temp_grid[x][y+1] = '.'
                            if y-1 >= 0:
                                temp_grid[x][y-1] = '.'
                            temp_grid[x][y] = '.'
        
            grid_list = copy.deepcopy(temp_grid)
        state += 1

    grid = ["".join(row) for row in grid_list]
    return grid    
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()





#!/bin/python3

import math
import os
import random
import re
import sys
import copy

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    
    rows, cols = len(grid), len(grid[0])
    if n % 2 == 0:
        foo = [['O' for _ in range(cols)] for _ in range(rows)]
        return ["".join(row) for row in foo]
    
    # rows, cols = len(grid), len(grid[0])
    grid_list = [list(row) for row in grid]
    temp_grid = [['O' for _ in range(cols)] for _ in range(rows)]
    state = 2   # 1
    while state <= n:
        print('Start of State: ', state)
        print('Temp Grid:')
        print(["".join(row) for row in temp_grid])
        print()
        print('Grid List:')
        print(["".join(row) for row in grid_list])
        print()
        # temp_grid = copy.deepcopy(grid_list) # make a copy of the grid state, and invert all of the states (bomb, not bomb)
        # temp_grid = [['O' if x == '.' else '.' for x in row] for row in temp_grid]

        # if n % 3 == 1:
        #     continue
        if state % 2 == 0:  # if n % 3 == 2:
            # temp_grid = copy.deepcopy(grid)
            temp_grid = [['O' for _ in range(cols)] for _ in range(rows)]
            
            # for i in range(rows):
            #     for j in range(cols):
            #         if j == 'O':
            #             grid_list[i][j] = '.'
            #         else:
            #             grid_list[i][j] = 'O'
            
            # grid_list = [['O' for _ in range(cols)] for _ in range(rows)]
            # print(["".join(row) for row in grid_list])
        else: 
        # if n % 2 != 0:
            # Here's where we do the math for destroying neighboring cells
            # temp_grid = [['O' for _ in range(cols)] for _ in range(rows)]
            # temp_grid = [['O' if x == '.' else '.' for x in row] for row in grid]
            
            # print('Grid List:')
            # print(["".join(row) for row in grid_list])
            # print()
            # print('Temp Grid BEFORE:')
            # print(["".join(row) for row in temp_grid])
            # print()
                
            for x in range(rows):
                for y in range(cols):
                    if grid[x][y] == 'O':
                        if grid[x][y] == 'O':
                            if x+1 < rows:
                                temp_grid[x+1][y] = '.'
                            if x-1 >= 0:
                                temp_grid[x-1][y] = '.'
                            if y+1 < cols:
                                temp_grid[x][y+1] = '.'
                            if y-1 >= 0:
                                temp_grid[x][y-1] = '.'
                            temp_grid[x][y] = '.'
        
            print('Temp Grid AFTER explosions:')
            print(["".join(row) for row in temp_grid])
            print()
            grid_list = copy.deepcopy(temp_grid)
        # print('Grid List:')
        # print(["".join(row) for row in grid_list])
        # print()
        # print('Temp Grid:')
        # print(["".join(row) for row in temp_grid])
        # print()
        state += 1
        # grid_list = copy.deepcopy(temp_grid)
        # print(["".join(row) for row in grid_list])
    grid = ["".join(row) for row in temp_grid]
    return grid    
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()




#!/bin/python3

import math
import os
import random
import re
import sys
import copy

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    
    rows, cols = len(grid), len(grid[0])
    if n % 2 == 0:
        foo = [['O' for _ in range(cols)] for _ in range(rows)]
        return ["".join(row) for row in foo]
    
    # rows, cols = len(grid), len(grid[0])
    grid_list = [list(row) for row in grid]
    state = 2   # 1
    while state <= n:
        print('State number: ', state)
        temp_grid = copy.deepcopy(grid_list) # make a copy of the grid state, and invert all of the states (bomb, not bomb)
        temp_grid = [['O' if x == '.' else '.' for x in row] for row in temp_grid]

        # if n % 3 == 1:
        #     continue
        # if state % 2 == 0:  # if n % 3 == 2:
            # temp_grid = copy.deepcopy(grid)
            
            # for i in range(rows):
            #     for j in range(cols):
            #         if j == 'O':
            #             grid_list[i][j] = '.'
            #         else:
            #             grid_list[i][j] = 'O'
            
            # grid_list = [['O' for _ in range(cols)] for _ in range(rows)]
            # print(["".join(row) for row in grid_list])
        # else: 
        if n % 2 != 0:
            # Here's where we do the math for destroying neighboring cells
            temp_grid = [['O' for _ in range(cols)] for _ in range(rows)]
            for x in range(rows):
                for y in range(cols):
                    if grid[x][y] == 'O':
                        if x+1 < rows and temp_grid[x+1][y] != 'O':
                            temp_grid[x+1][y] = '.'
                        if x-1 >= 0 and temp_grid[x-1][y] != 'O':
                            temp_grid[x-1][y] = '.'
                        if y+1 < cols and temp_grid[x][y+1] != 'O':
                            temp_grid[x][y+1] = '.'
                        if y-1 >= 0 and temp_grid[x][y-1] != 'O':
                            temp_grid[x][y-1] = '.'
        print('Grid List:')
        print(["".join(row) for row in grid_list])
        print()
        print('Temp Grid:')
        print(["".join(row) for row in temp_grid])
        print()
        state += 1
        grid_list = copy.deepcopy(temp_grid)
        # print(["".join(row) for row in grid_list])
    grid = ["".join(row) for row in grid_list]
    return grid    
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()












#!/bin/python3

import math
import os
import random
import re
import sys
import copy

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    rows, cols = len(grid), len(grid[0])
    grid_list = [list(row) for row in grid]
    state = 2   # 1
    while state <= n:
        temp_grid = copy.deepcopy(grid_list)    # make a copy of the grid state, and invert all of the states (bomb, not bomb)
        # if n % 3 == 1:
        #     continue
        if n % 2 == 0:  # if n % 3 == 2:
            # temp_grid = copy.deepcopy(grid)
            for i in range(rows):
                for j in range(cols):
                    if j == 'O':
                        grid_list[i][j] = '.'
                    else:
                        grid_list[i][j] = 'O'
        else: 
            # Here's where we do the math for destroying neighboring cells
            for x in range(rows):
                for y in range(cols):
                    if grid[x][y] == 'O':
                        if x+1 < rows:
                            temp_grid[x+1][y] = '.'
                        if x-1 >= 0:
                            temp_grid[x-1][y] = '.'
                        if y+1 < cols:
                            temp_grid[x][y+1] = '.'
                        if y-1 >= 0:
                            temp_grid[x][y-1] = '.'
        state += 1
        grid_list = copy.deepcopy(temp_grid)
    grid = ["".join(row) for row in grid_list]
    return grid    
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
