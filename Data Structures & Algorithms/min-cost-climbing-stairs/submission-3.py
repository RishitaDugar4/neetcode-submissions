class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        top down approach -> use recursion
        '''
        dp = [-1] * (len(cost)+1)

        def dfs(n, dp):
            if n < 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            dp[n] = cost[n] + min(dfs(n-1, dp), dfs(n-2, dp))
            return dp[n]

        return min(dfs(len(cost)-1, dp), dfs(len(cost)-2, dp))
            