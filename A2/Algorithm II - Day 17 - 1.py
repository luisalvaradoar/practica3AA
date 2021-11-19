class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        count = self.dpSolution(text1,len(text1),text2,len(text2))
        
        return count
    
    def recursive(self,s1,m,s2,n):
        if m<0 or n<0:
            return 0
        
        
        if s1[m] == s2[n]:
            return 1 + self.recursive(s1,m-1,s2,n-1)
        else:
            return max(self.recursive(s1,m,s2,n-1),self.recursive(s1,m-1,s2,n))
        
    def dpSolution(self,s1,m,s2,n):
        
        table = [[0 for i in range(m+1)] for j in range(n+1)]
        
        for row in range(1,n+1):
            for col in range(1,m+1):
                
                if s1[col-1] == s2[row-1]:
                    table[row][col] = 1 + table[row-1][col-1]
                else:
                    table[row][col] = max(table[row-1][col],table[row][col-1])

        return table[-1][-1]