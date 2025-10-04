#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    n = int(len(matrix) / 2)
    
    total = 0
    for i in range(n):
        for j in range(n):
            print(i, j)
            if j == i:
                total += max(matrix[i][j], matrix[i][-(j+1)], matrix[-(j+1)][j], matrix[-(j+1)][-(j+1)])
            elif j > i:
                total += max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)]) 
            elif j < i:
                total += max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)])

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()






# matrix = [  [112, 42, 83, 119], 
#             [56, 125, 56, 49], 
#             [15, 78, 101, 43], 
#             [62, 98, 114, 108]]
matrix = [  [112, 42, 83, 119, 130, 11], 
            [56, 125, 56, 49, 14, 55], 
            [15, 78, 101, 43, 69, 99], 
            [62, 98, 114, 108, 56, 24],
            [111, 59, 566, 14, 55, 18],
            [56, 23, 34, 78, 78, 48]]
# matrix = [  [112, 42, 83, 119, 56, 76, 97, 45, 63, 21],
#              [56, 125, 56, 49, 43, 67, 98, 24, 59, 30],
#              [15, 78, 101, 43, 60, 23, 91, 65, 80, 35],
#              [62, 98, 114, 108, 91, 60, 72, 43, 77, 23],
#              [13, 67, 89, 95, 64, 76, 88, 54, 67, 22],
#              [49, 85, 72, 65, 86, 84, 97, 45, 54, 31],
#              [56, 86, 99, 102, 34, 45, 78, 23, 54, 12],
#              [92, 108, 56, 67, 45, 34, 67, 28, 90, 13],
#              [45, 64, 79, 80, 34, 76, 99, 45, 58, 19],
#              [66, 87, 89, 91, 12, 45, 54, 23, 67, 11]   ]

n = int(len(matrix) / 2)
# count = sum(len(sublist) for sublist in matrix)
# unique = int(count / 4)

# n_full = len(matrix)
# total = 0
# for i in range(n_full):
#     for j in range(n_full)
#     total += max(matrix[i][i], matrix[i][n-(i+1)], matrix[n-(i+1)][i], matrix[n-(i+1)][n-(i+1)])

total = 0
for i in range(n):
    for j in range(n):
        print(i, j)
        if j == i:# and i == 0:
            print(1)
            print(matrix[i][j], matrix[i][-(j+1)], matrix[-(j+1)][j], matrix[-(j+1)][-(j+1)])
            print(max(matrix[i][j], matrix[i][-(j+1)], matrix[-(j+1)][j], matrix[-(j+1)][-(j+1)]))
            print()
            total += max(matrix[i][j], matrix[i][-(j+1)], matrix[-(j+1)][j], matrix[-(j+1)][-(j+1)])
        elif j > i:
        # elif j == 2: 
            print(2)
            print(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)])
            print(max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)]))
            print()
            total += max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)]) 
        # elif j >= 3: 
        # # else:
        #     print(3)
        #     print(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)])
        #     print(max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)]))
        #     print()
        #     total += max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)])
        elif j < i:
            print(4)
            print(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)])
            print(max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)]))
            print()
            total += max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)])

print(total)








# Write your code here
matrix = [  [112, 42, 83, 119], 
            [56, 125, 56, 49], 
            [15, 78, 101, 43], 
            [62, 98, 114, 108]]
# matrix = [  [112, 42, 83, 119, 130, 11], 
#             [56, 125, 56, 49, 14, 55], 
#             [15, 78, 101, 43, 69, 99], 
#             [62, 98, 114, 108, 56, 24],
#             [111, 59, 566, 14, 55, 18],
#             [56, 23, 34, 78, 78, 48]]

# print(matrix[0])
# exit()

n = int(len(matrix) / 2)
count = sum(len(sublist) for sublist in matrix)
unique = int(count / 4)

# print(matrix[0][1], matrix[0][-(1+1)], matrix[-(1)][1], matrix[-(1)][-(1+1)])
# exit()

total = 0
for i in range(n):
    for j in range(n):
        print(i, j)
        if j == 0 and i == 0:
            print(matrix[i][j], matrix[i][-(j+1)], matrix[-(j+1)][j], matrix[-(j+1)][-(j+1)])
            print(max(matrix[i][j], matrix[i][-(j+1)], matrix[-j][j], matrix[-j][-(j+1)]))
            print()
            total += max(matrix[i][j], matrix[i][-(j+1)], matrix[-(j+1)][j], matrix[-(j+1)][-(j+1)])
        elif i >= 1:
            print(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)])
            print(max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)]))
            print()
            total += max(matrix[i][j], matrix[i][-(j+1)], matrix[-(i+1)][j], matrix[-(i+1)][-(j+1)]) 
        # elif j == 1 and i == 1: 
            
        else:
            print(matrix[i][j], matrix[i][-(j+1)], matrix[-j][j], matrix[-j][-(j+1)])
            print(max(matrix[i][j], matrix[i][-(j+1)], matrix[-j][j], matrix[-j][-(j+1)]))
            print()
            total += max(matrix[i][j], matrix[i][-(j+1)], matrix[-j][j], matrix[-j][-(j+1)])

print(total)
            
            
            
# current_max = 0
# cm_row = []
# cm_col = []
# for i in matrix:
#     if max(i) > current_max and max(i) in i[:int(len(matrix) / 2)]:
#         cm_row = matrix.index(i)
#         cm_col = i.index(max(i))
#         current_max = 0
#     elif max(i) > current_max:
        
        
# print(cm_row, cm_col)
# exit()
        
    
# sum = 0
# mat_half = int(len(matrix))
# for m in range(mat_half):
#     for n in range(mat_half):
#         sum += matrix[m][n]
# print(sum)
# # return sum


# new_list = []
# new_list.append(matrix[0][0])
# new_list.append(matrix[0][-1])
# new_list.append(matrix[-1][0])
# new_list.append(matrix[-1][-1])
# print(new_list)
# print(max(new_list))


# for r in range(2 ^ (2 *len(matrix))):
#     sum = 0
#     mat_half = int(len(matrix))
#     for m in range(mat_half):
#         for n in range(mat_half):
#             sum += matrix[m][n]
#     # print(sum)
#     # return sum