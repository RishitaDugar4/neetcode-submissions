class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultSet = set()
        nums = sorted(nums)

        for i, a in enumerate(nums):
            left = i+1
            right = len(nums)-1

            while (left < right):
                if a + nums[left] + nums[right] == 0:
                    resultSet.add((a, nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif a + nums[left] + nums[right] > 0:
                    right -= 1

                elif a + nums[left] + nums[right] < 0:
                    left += 1

        return list(resultSet)

        