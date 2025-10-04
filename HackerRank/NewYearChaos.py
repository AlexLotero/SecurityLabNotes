def minimumBribes(q):
    # Write your code here
    # print(q)
    # q = [2, 1, 5, 3, 4]
    # print('Original:    ', q)

    q_edit = copy.deepcopy(q)
    q_edit.sort()

    # print('Sorted:      ', q_edit)

    # location = []
    # for i in q_edit:
    #     location.append(q.index(i))
        
    # print('Positions:   ', location)

    min_bribes = 0
    q_sort_iter = copy.deepcopy(q_edit)
    chaos = False

    for i in q_sort_iter:#[::-1]:
        iter = 0
        index_cur = q_edit.index(i)
        index_goal = q.index(i)
        difference = index_cur - index_goal
        # print(difference)
        if difference > 2:
            print('Too chaotic')
            chaos = True
            continue
            element = q_edit.pop(index_cur)
            q_edit.insert(index_goal, element)
            min_bribes += 2
            # print('Test:        ', q_edit)
            # exit()
        elif difference > 0:
            min_bribes += abs(difference)
    #     elif difference == 1:
    #         element = q_edit.pop(index_cur)
    #         q_edit.insert((index_cur-1), element)
    #         min_bribes += 1
    #         # print('Test:        ', q_edit)
    #         # exit()
    #     if q_edit == q:
    #         print(min_bribes)
    #         break
    #     iter += 1
    # if q_edit != q:
    #     print("Too chaotic")
    
    if not chaos:
        print(min_bribes)



import copy

# q = [2, 1, 5, 3, 4]
q = [1, 2, 5, 3, 7, 8, 6, 4]
print('Original:    ', q)
# print()


q_edit = copy.deepcopy(q)
q_edit.sort()

print('Sorted:      ', q_edit)
print()

# location = []
# for i in q_edit:
#     location.append(q.index(i))
    
# print('Positions:   ', location)

min_bribes = 0
q_sort_iter = copy.deepcopy(q_edit)
chaos = False

for i in q_sort_iter[::-1]:
    iter = 0
    index_cur = q_edit.index(i)
    index_goal = q.index(i)
    difference = index_cur - index_goal
    print('Difference; :', difference)
    if difference > 2:
        print('Too chaotic')
        chaos = True
        # continue
        element = q_edit.pop(index_cur)
        q_edit.insert(index_goal, element)
        min_bribes += 2
        print('Test:        ', q_edit)
        # exit()
    elif difference > 0:
        min_bribes += difference
#     elif difference == 1:
#         element = q_edit.pop(index_cur)
#         q_edit.insert((index_cur-1), element)
#         min_bribes += 1
#         # print('Test:        ', q_edit)
#         # exit()
#     if q_edit == q:
#         print(min_bribes)
#         break
#     iter += 1
    print('After iter ' + str(i) + ': ', q_edit)
# if q_edit != q:
#     print("Too chaotic")
if not chaos:
    print(min_bribes)



def minimumBribes(q):
    # Write your code here

    # q = [2, 1, 5, 3, 4]
    # print('Original:    ', q)

    q_edit = copy.deepcopy(q)
    q_edit.sort()

    # print('Sorted:      ', q_edit)

    # location = []
    # for i in q_edit:
    #     location.append(q.index(i))
        
    # print('Positions:   ', location)

    min_bribes = 0
    q_sort_iter = copy.deepcopy(q_edit)
    chaos = False

    for i in q_sort_iter[::-1]:
        iter = 0
        index_cur = q_edit.index(i)
        index_goal = q.index(i)
        difference = index_cur - index_goal
        if difference >= 2:
            # print('Too chaotic')
            # chaos = True
            # continue
            element = q_edit.pop(index_cur)
            q_edit.insert(index_goal, element)
            min_bribes += 2
            # print('Test:        ', q_edit)
            # exit()
        # elif difference > 0:
        #     min_bribes += difference
        elif difference == 1:
            element = q_edit.pop(index_cur)
            q_edit.insert((index_cur-1), element)
            min_bribes += 1
            # print('Test:        ', q_edit)
            # exit()
        if q_edit == q:
            print(min_bribes)
            break
        iter += 1
    if q_edit != q:
        print("Too chaotic")
    # if not chaos:
    #     print(min_bribes)



def minimumBribes(q):
    # Write your code here

    # q = [2, 1, 5, 3, 4]
    # print('Original:    ', q)

    q_edit = copy.deepcopy(q)
    q_edit.sort()

    # print('Sorted:      ', q_edit)

    # location = []
    # for i in q_edit:
    #     location.append(q.index(i))
        
    # print('Positions:   ', location)

    min_bribes = 0
    q_sort_iter = copy.deepcopy(q_edit)
    chaos = False

    for i in q_sort_iter[::-1]:
        iter = 0
        index_cur = q_edit.index(i)
        index_goal = q.index(i)
        difference = index_cur - index_goal
        if difference > 2:
            print('Too chaotic')
            chaos = True
            continue
            element = q_edit.pop(index_cur)
            q_edit.insert(index_goal, element)
            min_bribes += 2
            # print('Test:        ', q_edit)
            # exit()
        elif difference > 0:
            min_bribes += difference
    #     elif difference == 1:
    #         element = q_edit.pop(index_cur)
    #         q_edit.insert((index_cur-1), element)
    #         min_bribes += 1
    #         # print('Test:        ', q_edit)
    #         # exit()
    #     if q_edit == q:
    #         print(min_bribes)
    #         break
    #     iter += 1
    # if q_edit != q:
    #     print("Too chaotic")
    if not chaos:
        print(min_bribes)



# CURRENTLY WORKING??

import copy

q = [2, 1, 5, 3, 4]
print('Original:    ', q)

q_edit = copy.deepcopy(q)
q_edit.sort()
print('Sorted:      ', q_edit)

location = []

for i in q_edit:
    location.append(q.index(i))
    
print('Positions:   ', location)

min_bribes = 0
q_sort_iter = copy.deepcopy(q_edit)

for i in q_sort_iter[::-1]:
    iter = 0
    index_cur = q_edit.index(i)
    index_goal = q.index(i)
    difference = index_cur - index_goal
    if difference >= 2:
        element = q_edit.pop(index_cur)
        q_edit.insert(index_goal, element)
        min_bribes += 2
        print('Test:        ', q_edit)
        # exit()
    elif difference == 1:
        element = q_edit.pop(index_cur)
        q_edit.insert((index_cur-1), element)
        min_bribes += 1
        print('Test:        ', q_edit)
        # exit()
    if q_edit == q:
        print(min_bribes)
        break
    iter += 1
    # if 




# my_list = ['apple', 'banana', 'cherry', 'date']

# # Determine the index of the element you want to move
# index_to_move = my_list.index('cherry')

# # Remove the element from the original position
# element = my_list.pop(index_to_move)

# # Insert the element at the new position
# new_position = 1
# my_list.insert(new_position, element)

# print(my_list)