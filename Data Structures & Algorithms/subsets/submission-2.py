class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, currSet = [], []

        def helper(i, nums, subset, currSet):
            if i >= len(nums):
                subset.append(currSet.copy())
                return

            #decision to add
            currSet.append(nums[i])
            helper(i+1, nums, subset, currSet)
            currSet.pop()


            #decision to not add
            helper(i+1, nums, subset, currSet)

        helper(0, nums, subset, currSet)

        return subset