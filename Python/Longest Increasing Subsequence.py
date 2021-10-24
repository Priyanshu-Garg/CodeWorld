"""
Longest Increasing Subsequence

Given an array with N elements, you need to find the length of the 
longest subsequence of a given sequence such that all elements of 
the subsequence are sorted in strictly increasing order.

Input Format
    Line 1 : An integer N 
    Line 2 : Elements of arrays separated by spaces

Output Format
    Line 1 : Length of longest subsequence

Input Constraints
    1 <= n <= 10^3

Sample Input 1 :
    6
    5 4 11 1 16 8
Sample Output 1 :
    3
Sample Output Explanation
    Length of longest subsequence is 3 i.e. (5,11,16) or (4,11,16).

"""


def lis(arr): 
    n=len(arr)
    dp=[[0 for j in range(2)] for i in range(n+1)]
    
    for i in range(n-1,-1,-1):
        including_max=1
        for j in range(i+1,n):
            if li[j]>li[i]:
                including_max=max(including_max,1+dp[j][0])
        dp[i][0]=including_max
        excluding_max=dp[i+1][1]
        overallMax=max(including_max,excluding_max)
        dp[i][1]=overallMax
    return dp[0][1]

n = int(input())
li = [int(ele) for ele in input().split()]
print(lis(li))