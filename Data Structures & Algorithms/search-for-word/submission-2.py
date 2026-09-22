class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = set()

        def dfs(index, row, col):
            if (row, col) in visited:
                return False
            visited.add((row, col))
    
            if board[row][col] != word[index]:
                visited.remove((row, col))
                return False #early exit

            if index == len(word)-1:
                return True

            for nx, ny in directions:
                if nx+row < 0 or nx+row >= len(board) or ny+col < 0 or ny+col >= len(board[0]):
                    continue
                if board[nx+row][ny+col] != word[index+1]:
                    continue
                if (nx+row, ny+col) in visited:
                    continue

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

