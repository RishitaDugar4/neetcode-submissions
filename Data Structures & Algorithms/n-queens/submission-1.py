class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        queens have to be in separate columns, 
        separate rows, not diagonal from each other

        backtracking -> permutation
            - order matters

        board has to be at least n*n
        '''
        #queens can move in horizontal, vertical, diagonal position
        board = [["."] * n for i in range(n)]
        result = []

        def isValid(r, c, board):
            row = r-1
            while row >= 0:
                if board[row][c] == 'Q':
                    return False
                row -= 1
            
            row, col = r-1, c-1
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False

                row -= 1
                col -= 1

            row, col = r-1, c+1
            while row >= 0 and col < len(board):
                if board[row][col] == 'Q':
                    return False

                row -= 1
                col += 1

            return True

        def dfs(row):
            if row == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if isValid(row, c, board):
                    board[row][c] = "Q"
                    dfs(row+1)
                    board[row][c] = "."    

        dfs(0)
        return result
            
