class Solution:
    def climbStairs(self, n: int) -> int:
        #stairs go from 1 to n instead of 0 to n -> 0 to n01
        if n <= 2:
            return n
        dp = [0] * (n+1) #so not out of bounds. that last entry will be 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1): #want to include n, so we need n+1
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n] 