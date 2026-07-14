class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = len(nums)
        low, high = 0, len(nums)-1

        while (low <= high):
            mid = (low+high)//2

            if (nums[mid] == target):
                return mid

            elif (nums[mid] > target):
                high = mid-1
                result = mid

            else:
                low = mid+1

        return result