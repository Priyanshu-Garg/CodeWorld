"""
Matrix Chain Multiplication

Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most 
efficient way to multiply these matrices i.e. determine where to place parentheses 
to minimise the number of multiplications.

You will be given an array p[] of size n + 1. Dimension of matrix Ai is p[i - 1]*p[i]. 
You need to find minimum number of multiplications needed to multiply the chain.

Input Format :
    Line 1 : Integer n i.e. number of matrices
    Line 2 : n + 1 integers i.e. elements of array p[] 

Output Format :
    Line 1 : Minimum number of multiplication needed

Constraints :
    1 <= n <= 100

Sample Input 1 :
    3
    10 15 20 25
Sample Output :
    8000
Sample Output Explanation :
    There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
    If multiply in order A1*(A2*A3) then number of multiplications required are 15000.
    If multiply in order (A1*A2)*A3 then number of multiplications required are 8000.
    Thus minimum number of multiplications required are 8000
"""

import sys
def mcm(p,i,j,dp):
    if i==j:
        return 0
    min_value=sys.maxsize
    for k in range(i,j):
        if dp[i][k]==-1:
            ans1=mcm(p,i,k,dp)
            dp[i][k]=ans1
        else:
            ans1=dp[i][k]
        if dp[k+1][j]==-1:
            ans2=mcm(p,k+1,j,dp)
            dp[k+1][j]=ans2
        else:
            ans2=dp[k+1][j]
        mCost=p[i-1]*p[k]*p[j]
        curr_value=ans1+ans2+mCost
        min_value=min(min_value,curr_value)
    return min_value

n=int(input())
p=[int(ele) for ele in input().split()]
n=len(p)-1
dp=[[-1 for j in range(n+1)] for i in range(n+1)]
ans=mcm(p,1,n,dp)
print(ans)