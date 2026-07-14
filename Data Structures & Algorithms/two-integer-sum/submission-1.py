class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numSum = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numSum:
                return [numSum[complement], i]
            else:
                numSum[nums[i]] = i

        