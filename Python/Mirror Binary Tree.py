"""
-----------------------------------------  Mirror Binary Tree  -------------------------------------------

Mirror the given binary tree. That is, right child of every nodes should become left and left should become
right.

Note : 
    You don't need to print or return the tree, just mirror it.

#### Input format :
    Line 1 : Elements in level order form (separated by space)

    (If any node does not have left or right child, take -1 in its place)

#### Output format : 
    Elements in level order form (Every level in new line)

#### Sample Input 1:
    1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
#### Sample Output 1:
    1 
    3 2 
    7 6 5 4

#### Sample Input 2:
    5 10 6 2 3 -1 -1 -1 -1 -1 9 -1 -1
#### Sample Output 2:
    5 
    6 10 
    3 2 
    9
"""

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirrorBinaryTree(root):

    if root is None:
        return 

    root.left,root.right=root.right,root.left

    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)
    

def buildLevelTree(levelorder):
    
    index = 0
    length = len(levelorder)

    if length<=0 or levelorder[0]==-1:
        return None

    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)

    while not q.empty():

        currentNode = q.get()
        leftChild = levelorder[index]

        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelorder[index]

        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

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
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
mirrorBinaryTree(root)
printLevelATNewLine(root)


