class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
        queue = deque() #bfs implementation
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r,c)) #[(0, 2), (3, 0)]


        while queue: #(0, 2)
            x, y = queue.popleft()
            for i in directions:
                if x+i[0] >= len(grid) or x+i[0] < 0 or y+i[1] >= len(grid[0]) or y+i[1] < 0 or grid[x+i[0]][y+i[1]] == -1:
                    continue
                
                if grid[x+i[0]][y+i[1]] == 2147483647:
                    queue.append((x+i[0],y+i[1]))
                    grid[x+i[0]][y+i[1]] = grid[x][y] + 1

        