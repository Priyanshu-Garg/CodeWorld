"""
----------------------------  Code : BFS Traversal  -------------------------------

Given an undirected and disconnected graph G(V, E), print its BFS traversal.
Here you need to consider that you need to print BFS path starting from vertex 0 only.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.

Note : 
    1. Take graph input in the adjacency matrix.
    2. Handle for Disconnected Graphs as well

Input Format :
    Line 1: Two Integers V and E (separated by space)
    Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that 
    there exists an edge between Vertex 'a' and Vertex 'b'. 

Output Format :
    BFS Traversal (separated by space)

Constraints :
    2 <= V <= 1000
    1 <= E <= 1000

Sample Input 1:
    4 4
    0 1
    0 3
    1 2
    2 3
Sample Output 1:
    0 1 3 2
"""

import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]
        
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        
    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
        
    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False
    
    def __str__(self):
        return str(self.adjMatrix)
    
    def bfs(self):
        q=queue.Queue()
        visited=[False for i in range(self.nVertices)]
        for j in range(self.nVertices):
            if visited[j] is False:
                q.put(j)
                visited[j]=True
        
                while q.empty() is False:
                    v=q.get()
                    print(v, end = " ")
                    for i in range(self.nVertices):
                        if self.adjMatrix[v][i] > 0 and visited[i] is False:
                            q.put(i)
                            visited[i] = True
        '''def bfs(self):
        q=queue.Queue()
        visited=[False for i in range(self.nVertices)]
        
        q.put(0)
        visited[0]=True
        while q.empty() is False:
            a=q.get()
            print(a,end=" ")
            for i in range(self.nVertices):
                if (self.adjMatrix[a][i]>0 and visited[i] is False):
                    q.put(i)
                    visited[i]=True'''
#Main        
ve=[int(ele) for ele in input().split()]
g=Graph(ve[0])
for i in range(ve[1]):
    el=[int(ele) for ele in input().split()]
    g.addEdge(el[0],el[1])
g.bfs()