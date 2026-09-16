class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set() #empty
        numIslands = 0 #0

        def dfs(x, y): #right, down, left, up
            if (x, y) in seen:
                return #early exit
            else:
                seen.add((x, y))
                
            for i in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if x+i[0] >= len(grid) or y+i[1] >= len(grid[0]) or x+i[0] < 0 or y+i[1] < 0: 
                    #right, down, left, up
                    continue
                if grid[x+i[0]][y+i[1]] == '1':
                    dfs(x+i[0], y+i[1])
            
            return 


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    if (r, c) not in seen:
                        numIslands += 1
                    dfs(r, c)
                else:
                    continue

        return numIslands