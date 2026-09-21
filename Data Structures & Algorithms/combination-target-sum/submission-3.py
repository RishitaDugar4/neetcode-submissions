class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        subsets = []

        def helper(index, subsets, currSet, runningSum):
            #early exit conditions
            if runningSum > target:
                return

            if index >= len(nums):
                return
            
            #base case
            if runningSum == target:
                subsets.append(currSet.copy())
                return

            #recursive condition
            for j in range(index, len(nums)): #start at index to avoid duplicate values
                if runningSum + nums[j] > target:
                    return

                
                currSet.append(nums[j])
                helper(j, subsets, currSet, runningSum + nums[j])
                #until you iterate to next value, can reuse j
                currSet.pop()
                #runningSum -= nums[j]

        helper(0, subsets, [], 0)
        return subsets