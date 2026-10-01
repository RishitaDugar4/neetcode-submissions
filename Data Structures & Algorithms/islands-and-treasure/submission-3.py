class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        use bfs
            - enqueue when 0
            - 
        '''
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        continue

                    if grid[nr][nc] == 2147483647:
                        queue.append((nr, nc))
                        grid[nr][nc] = grid[r][c] + 1