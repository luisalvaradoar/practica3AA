class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        if grid[0][0] == 1:
            return -1
        
        def check(i, j):
            return 0 <= i < rows and 0 <= j < cols and grid[i][j] == 0
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        queue = [(0,0,1)]
        
        while queue:
            tmp = len(queue)
            for i in range(tmp):
                x,y,cost = queue.pop(0)
                
                if x == rows-1 and y == cols-1:
                    return cost
                
                for dx,dy in dirs:
                    nx, ny = x+dx, y+dy
                    
                    if not check(nx,ny):
                        continue
                        
                    queue.append((nx,ny,cost+1))
                    grid[nx][ny] = 1
                        
                    
        return -1