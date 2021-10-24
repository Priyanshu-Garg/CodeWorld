"""
------------------------------  LCS - Problem  -----------------------------------

Given two strings S1 and S2 with lengths M and N respectively, find the length 
of the longest common subsequence.

A subsequence of a string S whose length is K, is a string containing characters 
in same relative order as they are present in S, but not necessarily contiguous. 

Subsequences contain all the strings of length varying from 0 to K. For example, 
subsequences of string "abc" are -- ""(empty string), a, b, c, ab, bc, ac, abc.

Input Format :
    Line 1: String S1
    Line 2: String s2

Output Format :
    Length of the longest common subsequence.

Constraints :
    1 <= M <= 100
    1 <= N <= 100
    Time Limit: 1 sec

Sample Input 1:
    adebc
    dcadb
Sample Output 1:
    3
Explanation of Sample Input 1:
    "a", "d", "b", "c", "ad", "ab", "db", "dc" and "adb" are present as a 
    subsequence in both the strings in which "adb" has the maximum length. 
    There are no other common subsequence of length greater than 3 and hence the answer.

Sample Input 2:
    abcd
    acbdef
Sample Output 2:
    3
Explanation of Sample Input 2:
    "a", "b", "c", "d", "ab", "ac", "ad", "bd", "cd", "abd" and "acd" are present 
    as a subsequence in both the strings S1 and S2 in which "abd" and "acd" 
    are of the maximum length. There are no other common subsequence of length 
    greater than 3 and hence the answer.
"""


def lcsDP(s1, s2):
    n=len(s1)
    m=len(s2)
    dp=[[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if s1[i]==s2[j]:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j+1])
    return dp[0][0]
    
s1 =input().strip()
s2 =input().strip()
print(lcsDP(s1, s2))