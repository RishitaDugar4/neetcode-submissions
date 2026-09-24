class Solution:
    def rob(self, nums: List[int]) -> int:
        seen = [-1] * len(nums)

        def dfs(index):
            if index >= len(nums):
                return 0

            if seen[index] != -1:
                return seen[index]

            seen[index] = max(dfs(index+1), nums[index]+dfs(index+2))
            return seen[index]

        return dfs(0)

            