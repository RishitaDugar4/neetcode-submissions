class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {}
        def dfs(step):
            if step in seen: 
                return seen[step]

            if step >= n:
                return step == n

            seen[step] = dfs(step+1) + dfs(step+2)
            return seen[step]

        return dfs(0)
