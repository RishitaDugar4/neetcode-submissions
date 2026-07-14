class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        array of length n
        originally sorted in ascending order
        rotated between 1 and n times
        '''
        
        minimum = nums[0];

        for i in range(1, len(nums)):
            if nums[i] < minimum:
                minimum = nums[i]

        return minimum



