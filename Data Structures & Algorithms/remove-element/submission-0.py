class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        remove all occurences of val from nums in place --> 
            no new array for deletion
        then
        return the number of remaining elements such that the 
            first k elements of nums don't contain val
        '''
        i = 0
        j = 0
        while i < len(nums):
            print(nums)
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        
        nums = nums[0:j]
        return j



        