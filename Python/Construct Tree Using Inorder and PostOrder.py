"""
-------------------------------  Construct Tree Using Inorder and PostOrder  ------------------------------

Given Postorder and Inorder traversal of a binary tree, create the binary tree associated with the 
traversals.
You just need to construct the tree and return the root.

Note: 
    Assume binary tree contains only unique elements.

#### Input format :
    Line 1 : n (Total number of nodes in binary tree)
    Line 2 : Post order traversal
    Line 3 : Inorder Traversal
#### Output Format :
    Elements are printed level wise, each level in new line (separated by space).

#### Sample Input :
    8
    8 4 5 2 6 7 3 1
    4 8 2 5 1 6 3 7
#### Sample Output :
    1 
    2 3 
    4 5 6 7 
    8
"""

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder):

    if len(postorder)==0:
        return None
    root=BinaryTreeNode(postorder[-1])
    
    rootindex=-1
    for i in range(0,len(inorder)):
        if inorder[i]==root.data:
            rootindex=i
            break
            
    if rootindex==-1:
        return None
            
    leftinorder=inorder[0:rootindex]
    rightinorder=inorder[rootindex+1:]
    
    l=len(leftinorder)
    
    rightpostorder=postorder[l:len(postorder)-1]
    leftpostorder=postorder[:l]

    ltree=buildTreePostOrder(leftpostorder,leftinorder)
    rtree=buildTreePostOrder(rightpostorder,rightinorder)
    
    root.left=ltree
    root.right=rtree

    return root

def printLevelATNewLine(root):

    if root==None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()

    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()

            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
                
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
n=int(input())
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)
