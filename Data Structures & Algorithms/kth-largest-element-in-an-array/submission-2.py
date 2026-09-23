class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        heap -> heapify nums
        '''

        minheap = []
        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, num)
            elif num > minheap[0]:
                heapq.heapreplace(minheap, num)

        return minheap[0]
