class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(x, y):
            if grid[x][y] == 0:
                return 0
            else:
                grid[x][y] = 0
                area = 1


            for i in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if x+i[0] >= len(grid) or x+i[0] < 0 or y+i[1] >= len(grid[0]) or y+i[1] < 0:
                    continue

                if grid[x+i[0]][y+i[1]] == 1:
                    area += dfs(x+i[0], y+i[1])

            return area


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea