class Solution:
    def rob(self, nums: List[int]) -> int:
        seen = [-1] * (len(nums))
        

        def dfs(i):
            if i >= len(nums):
                return 0
            if seen[i] != -1:
                return seen[i]

            seen[i] = max(dfs(i+1), nums[i]+dfs(i+2))
            return seen[i]

        return dfs(0)

        
