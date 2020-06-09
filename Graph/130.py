# 130. Surrounded Regions

# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X

# Explanation:
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

class Solution(object):
    def solve(self, board):
        if len(board) == 0 or len(board[0]) == 0: return
        if len(board) < 3 or len(board[0]) < 3: return
        
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            if board[i][0] == 'O':
                self.boundaryDFS(board, i, 0)
            if board[i][m - 1] == 'O':
                self.boundaryDFS(board, i, m - 1)
                
        for j in range(m):
            if board[0][j] == 'O':
                self.boundaryDFS(board, 0, j)
            if board[n - 1][j] == 'O':
                self.boundaryDFS(board, n - 1, j)
                
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'
                    
                    
    def boundaryDFS(self, board, i, j):
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or board[i][j] != 'O':
            return
        
        board[i][j] = '*'
        self.boundaryDFS(board, i + 1, j)
        self.boundaryDFS(board, i - 1, j)
        self.boundaryDFS(board, i, j + 1)
        self.boundaryDFS(board, i, j - 1)

sol = Solution()
sol.solve([["X","O","X","O","X","O"]
        ,  ["O","O","O","X","O","X"],
           ["X","O","X","O","O","X"],
           ["O","X","O","X","X","X"]])