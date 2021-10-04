"""
------------------------------------------- Find a Node in Linked List -----------------------------------

You have been given a singly linked list of integers. Write a function that returns the index/position of 
an integer data denoted by 'N'(if it exists). -1 otherwise.

Note :
    Assume that the Indexing for the singly linked list always starts from 0.

#### Input format :
    *The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
     Then the test cases follow.
    *The first line of each test case or query contains the elements of the singly linked list separated by 
     a single space. 
    *The second line contains the integer value 'N'. It denotes the data to be searched in the given singly 
     linked list.

    Remember/Consider :
        While specifying the list elements for input, -1 indicates the end of the singly linked list and
        hence, would never be a list element.

#### Output format :
    *For each test case/query, print the index/position of 'N' in the singly linked list. -1, otherwise.
    *Output for every test case will be printed in a seperate line.

#### Constraints :
    1 <= t <= 10^2
    0 <= M <= 10^5
    Time Limit: 1sec
    Where 'M' is the size of the singly linked list.

#### Sample Input 1 :
    2
    3 4 5 2 6 1 9 -1
    5
    10 20 30 40 50 60 70 -1
    6
#### Sample Output 1 :
    2
    -1

#### Sample Input 2 :
    1
    3 4 5 2 6 1 9 -1
    6
#### Sample Output 2 :
    4
 Explanation for Sample Input 2 :
        For the given singly linked list, considering the indices starting from 0, progressing in a left 
        to right manner with a jump of 1, then the N = 6 appears at position 4.
"""

''' Time Complexity : O(n) 
    Space Complexity : O(1) 
        Where 'n' is the size of the Singly Linked List 
'''

from sys import stdin

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findNode(head, n) : 
    if head is None : 
        return -1 
    i = 0 
    while head is not None : 
        if head.data == n : 
            return i
        i += 1 
        head = head.next 
    return -1

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
    n = int(stdin.readline().rstrip()) 
    print(findNode(head, n)) 
    t -= 1