class Solution:
    def count(self, S, m, n): 
        table = [0]*(n+1)
        table[0] = 1
        for i in range(0,m):
            for j in range(S[i],n+1):
                table[j] += table[j-S[i]]
        return table[n] 