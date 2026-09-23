class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        use heap
        - first element is closest
        - every element is farther
        '''
        heap = []
        result = []
        for x, y in points:
            dist = x**2 + y**2
            heap.append((dist, x, y))

        heapq.heapify(heap)

        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result

        