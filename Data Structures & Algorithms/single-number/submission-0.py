class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            unique = True
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    unique = False
                    break

            if unique: return nums[i]