class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #key: value, value: index

        for i, num in enumerate(nums): #i = index, num = value
            complement = target - num
            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i
        return
            