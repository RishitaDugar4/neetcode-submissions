class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (1, 0), (-1,0)]
        queue = deque()
        num_ones = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))

                elif grid[r][c] == 1:
                    num_ones += 1
        
        while queue and num_ones > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for i in directions:
                    if x+i[0] >= len(grid) or x+i[0] < 0 or y+i[1] >= len(grid[0]) or y+i[1] < 0:
                        continue

                    if grid[x+i[0]][y+i[1]] == 1:
                        queue.append((x+i[0], y+i[1])) 
                        grid[x+i[0]][y+i[1]] = 2
                        num_ones -= 1

            time += 1

        if num_ones == 0:
            return time
        else:
            return -1

                

        