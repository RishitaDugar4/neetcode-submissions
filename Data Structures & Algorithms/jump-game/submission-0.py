class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1 #leftmost index that we need to reach

        for i in range(len(nums) - 2, - 1, -1):
            if i + nums[i] >= target:
                target = i
        
        return target == 0

        '''
        i = 3
        target = 5-1 = 4
        len(nums) = 5-2 = 3
        i = 3, nums[i] = 1 => 1 + 3 = 4 >= 4 yes
        target = i = 3

        i = 2
        i = 2, nums[i] = 0, 2 + 0 >= 3 skip

        i = 1
        i = 1, nums[i] = 2, 1 + 2 >= 3 yes
        target = i = 1

        i = 0
        i = 0, nums[i] = 1, 1 + 0 >= 1 yes
        target = i = 0

        target = 0

        '''