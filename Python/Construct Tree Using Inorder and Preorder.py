"""
---------------------------------  Construct Tree Using Inorder and Preorder  ------------------------------

Given Preorder and Inorder traversal of a binary tree, create the binary tree associated with the traversals.
You just need to construct the tree and return the root.

Note: 
    Assume binary tree contains only unique elements.

#### Input format :
    Line 1 : n (Total number of nodes in binary tree)
    Line 2 : Pre order traversal
    Line 3 : Inorder Traversal
#### Output Format :
    Elements are printed level wise, each level in new line (separated by space).

#### Sample Input :
    12
    1 2 3 4 15 5 6 7 8 10 9 12
    4 15 3 2 5 1 6 10 8 7 9 12
#### Sample Output :
    1 
    2 6 
    3 5 7 
    4 8 9 
    15 10 12
"""

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePreOrder(preorder, inorder):

    if len(preorder)==0:
        return None
    root=BinaryTreeNode(preorder[0])
    
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
    
    leftpreorder=preorder[1:l+1]
    rightpreorder=preorder[l+1:]
    
    ltree=buildTreePreOrder(leftpreorder,leftinorder)
    rtree=buildTreePreOrder(rightpreorder,rightinorder)
    
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
preorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePreOrder(preorder, inorder)
printLevelATNewLine(root)
