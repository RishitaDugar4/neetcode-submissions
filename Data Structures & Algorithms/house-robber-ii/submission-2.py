class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(nums):
            if not nums:
                return 0

            if len(nums) == 1:
                return nums[0]

            dp = [0] * (len(nums)+1)
            dp[1] = nums[0]

            for i in range(2, len(nums)+1):
                dp[i] = max(dp[i-1], nums[i-1]+dp[i-2])

            return dp[len(nums)]

        return max(dfs(nums[1:]), dfs(nums[:-1]))
