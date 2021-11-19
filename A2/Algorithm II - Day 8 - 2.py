class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def mark_not_surrounded(i: int, j: int):
            board[i][j] = "B"
            if i > 0 and board[i-1][j] == "O":
                mark_not_surrounded(i-1, j)
            if i < m-1 and board[i+1][j] == "O":
                mark_not_surrounded(i+1, j)
            if j > 0 and board[i][j-1] == "O":
                mark_not_surrounded(i, j-1)
            if j < n-1 and board[i][j+1] == "O":
                mark_not_surrounded(i, j+1)
        
        for i in range(m):
            for j in [0, n-1]:
                if board[i][j] == "X" or board[i][j] == "B":
                    continue
                mark_not_surrounded(i,j)
        for j in range(n):
            for i in [0, m-1]:
                if board[i][j] == "X" or board[i][j] == "B":
                    continue
                mark_not_surrounded(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "B":
                    board[i][j] = "O"

        return