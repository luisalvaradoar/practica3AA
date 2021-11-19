class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
         
        
        def backtrack(cur, index = 0):
            
            seen.add(cur)
            if index == len(word)-1:
                return True
            
            x,y = cur
            
            
            for i,j in directions:
                
                a = x + i
                b = y + j
                
                if 0 <= a < n and 0 <= b < m and (a,b) not in seen and board[a][b] == word[index + 1]:
                    if backtrack((a,b), index + 1):
                        return True
                    seen.remove((a,b))
                
                   
        m = len(board[0])
        n = len(board)
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        for i, row in enumerate(board):
            for i2, cell in enumerate(row):
                if cell == word[0]:
                    seen = set()
                    if backtrack((i,i2)):
                        return True