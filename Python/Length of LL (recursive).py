"""
-------------------------------- Length of LL (recursive) -------------------------------

Given a linked list, find and return the length of input LL recursively.

#### Input format :
    Linked list elements (separated by space and terminated by -1)

#### Output format :
    Length of LL

#### Sample Input :
    3 4 5 2 6 1 9 -1
#### Sample Output :
    7
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def lengthRecursive(head):
    if head==None:
        return 0
    return 1 + lengthRecursive(head.next)

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
len=lengthRecursive(l)
print(len)
