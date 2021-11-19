class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        zeros = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        
        q = deque(zeros)
        lvl_num = 1
        while q:
            l = len(q)
            for _ in range(l):
                x, y = q.popleft()
                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0<=nx<m and 0<=ny<n and mat[nx][ny] > 0:
                        mat[nx][ny] = -lvl_num
                        q.append((nx, ny))
            lvl_num += 1
     
        return [[-mat[i][j] for j in range(n)] for i in range(m)]