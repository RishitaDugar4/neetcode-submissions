class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [False] * len(nums)
        result = []

        def backtrack(currPath, used):
            if len(currPath) == len(nums):
                result.append(currPath[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                currPath.append(nums[i])
                backtrack(currPath, used)
                currPath.pop()
                used[i] = False #backtrack

        backtrack([], used)

        return result
        