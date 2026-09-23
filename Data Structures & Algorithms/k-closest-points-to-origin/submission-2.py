class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        use heap
        - first element is closest
        - every element is farther
        '''
        max_heap = []
        for x, y in points:
            dist = x**2 + y**2
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, [x, y]))
            elif dist < -max_heap[0][0]:
                heapq.heapreplace(max_heap, (-dist, [x, y]))

        return [point for _, point in max_heap]

        