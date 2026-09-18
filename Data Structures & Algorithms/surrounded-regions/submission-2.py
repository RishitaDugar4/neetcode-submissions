class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            board[r][c] = 'E'

            for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if r+i[0] >= len(board) or r+i[0] < 0 or c+i[1] >= len(board[0]) or c+i[1] < 0:
                    continue

                if board[r+i[0]][c+i[1]] == 'O':
                    dfs(r+i[0], c+i[1])


        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)

            if board[r][COLS-1] == 'O':
                dfs(r, COLS-1)

        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
            
            if board[ROWS-1][c] == 'O':
                dfs(ROWS-1, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'E':
                    board[r][c] = 'O'
        