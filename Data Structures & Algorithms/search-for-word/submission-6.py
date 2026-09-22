class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        if len(word) > ROWS * COLS:
            return False


        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = set()

        def dfs(index, row, col):            
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited or board[row][col] != word[index]:
                return False

            visited.add((row, col))
            if index == len(word)-1:
                return True

            for nx, ny in directions:
                if dfs(index+1, nx+row, ny+col):
                    return True

            visited.remove((row,col))
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(0, r, c):
                        return True


        return False

