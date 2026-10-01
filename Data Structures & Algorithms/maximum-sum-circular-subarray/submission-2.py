class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        non circular solution:

        maxSum = nums[0]
        currSum = 0

        for num in nums:
            currSum = max(0, currSum)
            currSum += num
            maxSum = max(maxSum, currSum)

        return maxSum

        circular case:
            - solution can either be in middle of wraparound
                or can be on the edges
            - total = included (wraparound) - excluded (middle)
            - wraparoound = total - excluded
            - excluded needs to be as small as possible to make included the max
                
        '''
        maxNum, minNum = nums[0], nums[0]
        currMax, currMin = 0, 0
        total = sum(nums)

        for num in nums:
            currMax = max(num, currMax + num)
            currMin = min(num, currMin + num)
            maxNum = max(maxNum, currMax)
            minNum = min(minNum, currMin)

        if maxNum > 0:
            return max(maxNum, total - minNum) 

        else:
            return maxNum




        # this solves the noncircular case
        # 
