#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    # Write your code here
    i = llist
    head = None
    while i:
        upcoming = i.next
        i.next = head
        head = i
        i = upcoming
    return head 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()

# =======================
# Walkthrough Example:
# =======================

# Input:
1 → 2 → 3 → 4 → None

# Initial State:
i = 1 (current node)
head = None


# Iteration 1:
upcoming = i.next  (store next node: upcoming = 2)
i.next = head      (1.next now points to None)
head = i           (head now points to 1)
i = upcoming       (move to next node, i = 2)

# After Iteration 1:
head: 1 → None
i: 2 → 3 → 4 → None


# Iteration 2:
upcoming = i.next  (store next node: upcoming = 3)
i.next = head      (2.next now points to 1)
head = i           (head now points to 2)
i = upcoming       (move to next node, i = 3)

# After Iteration 2:
head: 2 → 1 → None
i: 3 → 4 → None

# ...