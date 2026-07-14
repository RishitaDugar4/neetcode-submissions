class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        non-decreasing order
        remove duplicates in place

        can i use a dictionary to calculate this?
        numsdict = {num : }
        '''

        if not nums:
            return 0

        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1

        return index
            
        
        

        