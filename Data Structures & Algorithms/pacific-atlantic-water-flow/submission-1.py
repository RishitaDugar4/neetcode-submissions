class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        water can flow in 4 directions
            up down left right
        if height equal or lower [<=]
        '''
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pacific = set()
        atlantic = set()
        results = []
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(x, y, visit):
            if (x, y) in visit:
                return #early exit
            else:
                visit.add((x, y))

            for i in directions:
                if x+i[0] >= ROWS or x+i[0] < 0 or y+i[1] >= COLS or y+i[1] < 0:
                    continue

                if heights[x][y] <= heights[x+i[0]][y+i[1]]:
                    dfs(x+i[0], y+i[1], visit)

        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS-1, c, atlantic)

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS-1, atlantic)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    results.append([r, c])
        
        return results



        