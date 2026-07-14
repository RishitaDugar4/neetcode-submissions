class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()

        for i, a in enumerate(nums):
            left = i+1
            right = len(nums)-1

            while (left < right):
                if (a + nums[left] + nums[right] == 0):
                    result.add((a, nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif (a + nums[left] + nums[right] > 0):
                    right -= 1

                else:
                    left += 1

        return list(result)