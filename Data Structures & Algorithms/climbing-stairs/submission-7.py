class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {}

        def dfs(step):
            if step in seen:
                return seen[step]

            if step <= 2:
                seen[step] = step
                #seen[1] = 1
                #seen[2] = 2
                return seen[step]


            seen[step] = dfs(step-1) + dfs(step-2)

            return seen[step]
        
        return dfs(n)
