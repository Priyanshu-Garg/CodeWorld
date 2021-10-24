"""
---------------------------------------  Palindrome LinkedList  ------------------------------------------

You have been given a head to a singly linked list of integers. Write a function check to whether the list 
given is a 'Palindrome' or not.

#### Input format :
    *The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
     Then the test cases follow.
    *The first and the only line of each test case or query contains the elements(in ascending order) of 
     the singly linked list separated by a single space.
 
    Remember/Consider :
        While specifying the list elements for input, -1 indicates the end of the singly linked list and 
        hence, would never be a list element.
 
#### Output format :
    For each test case, the only line of output that print 'true' if the list is Palindrome or 'false' 
    otherwise

#### Constraints :
    1 <= t <= 10^2
    0 <= M <= 10^5
    Time Limit: 1sec
    Where 'M' is the size of the singly linked list.

#### Sample Input 1 :
    1
    9 2 3 3 2 9 -1
#### Sample Output 1 :
    true

#### Sample Input 2 :
    2
    0 2 3 2 5 -1
    -1
#### Sample Output 2 :
    false
    true
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

def reverseLinkedList(head) : 
    curr = head 
    prev = None 
    fwd = None

    while curr is not None : 
        fwd = curr.next 
        curr.next = prev 
        prev = curr 
        curr = fwd 

    return prev

def isPalindrome(head) : 
    if head is None or head.next is None : 
        return True 

    #find list center 
    fast = head 
    slow = head 
    while fast.next is not None and fast.next.next is not None : 
        fast = fast.next.next 
        slow = slow.next 
        
    secondHead = slow.next 
    slow.next = None 
    secondHead = reverseLinkedList(secondHead) 
    
    #compare two sublists now 
    firstSubList = secondHead 
    secondSubList = head 
    
    while firstSubList is not None : 
        if firstSubList.data != secondSubList.data : 
            return False 
            
        firstSubList = firstSubList.next 
        secondSubList = secondSubList.next 
        
    #Rejoin the two sublists to restore the input list to its original form 
    firstSubList = head 
    secondSubList = reverseLinkedList(secondHead) 

    while firstSubList.next is not None : 
        firstSubList = firstSubList.next 

    firstSubList.next = secondSubList 
    return True

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
    if isPalindrome(head) : 
        print('true') 
    else : 
        print('false') 
    t -= 1