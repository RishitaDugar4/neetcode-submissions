class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS = len(board)
        COLS = len(board[0])
        queue = deque()

        for r in range(ROWS):
            if (r,0) in queue or (r, COLS-1) in queue:
                continue
            
            if board[r][0] == 'O':
                queue.append((r, 0))

            if board[r][COLS-1] == 'O':
                queue.append((r, COLS-1))

        for c in range(COLS):
            if (0, c) in queue or (ROWS-1, c) in queue:
                continue

            if board[0][c] == 'O':
                queue.append((0, c))

            if board[ROWS-1][c] == 'O':
                queue.append((ROWS-1, c))

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                board[x][y] = 'E'

                for i in directions:
                    if x+i[0] < 0 or x+i[0] >= ROWS or y+i[1] < 0 or y+i[1] >= COLS:
                        continue

                    if board[x+i[0]][y+i[1]] == 'O':
                        queue.append((x+i[0], y+i[1]))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

                elif board[r][c] == 'E':
                    board[r][c] = 'O'

                    
