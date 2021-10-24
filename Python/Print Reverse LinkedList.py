"""
-------------------------------------- Print Reverse LinkedList ---------------------------------------

You have been given a singly linked list of integers. Write a function to print the list in a reverse order.
To explain it further, you need to start printing the data from the tail and move towards the head of the 
list, printing the head data at the end.

Note :
    You can’t change any of the pointers in the linked list, just print it in the reverse order.

#### Input format :
    *The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
     Then the test cases follow.
    *The first and the only line of each test case or query contains the elements(in ascending order) of 
     the singly linked list separated by a single space.
 
    Remember/Consider :
        While specifying the list elements for input, -1 indicates the end of the singly linked list and 
        hence, would never be a list element.
 
#### Output format :
    * For each test case/query, print the resulting singly linked list of integers in a row, separated by
     a single space.
    * Output for every test case will be printed in a seperate line.

#### Constraints :
    1 <= t <= 10^2
    0 <= M <= 10^3
    Time Limit: 1sec
    Where 'M' is the size of the singly linked list.

#### Sample Input 1 :
    1
    1 2 3 4 5 -1
#### Sample Output 1 :
    5 4 3 2 1

#### Sample Input 2 :
    2
    1 2 3 -1
    10 20 30 40 50 -1
#### Sample Output 2 :
    3 2 1
    50 40 30 20 10
"""

''' Time Complexity : O(n) 
    Space Complexity : O(n) 
        Where 'n' is the size of the Singly Linked List 
'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printReverse(head) : 
    if head is None : 
        return 
    printReverse(head.next) 
    print(head.data, end = " ")

def takeInput() : 
    head = None 
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0 
    while (i < len(datas)) and (datas[i] != -1) : 
        data = datas[i] 
        newNode = Node(data)

        if head is None : 
            head = newNode 
            tail = newNode 
        else : 
            tail.next = newNode 
            tail = newNode

        i += 1 
    return head

def printLinkedList(head) : 
    while head is not None : 
        print(head.data, end = " ") 
        head = head.next 
    print()

#main 
t = int(stdin.readline().rstrip()) 
while t > 0 :
    head = takeInput() 
    printReverse(head) 
    t -= 1
