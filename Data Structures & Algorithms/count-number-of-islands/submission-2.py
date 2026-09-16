class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0

        def dfs(x, y):
            if grid[x][y] == '0':
                return
            else:
                grid[x][y] = '0'

            for i in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if x+i[0] >= len(grid) or x+i[0] < 0 or y+i[1] >= len(grid[0]) or y+i[1] < 0:
                    continue
                dfs(x+i[0], y+i[1])
            return 
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    numIslands += 1
                    dfs(r, c)
    
        return numIslands