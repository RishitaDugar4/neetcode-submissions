class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounter = Counter(tasks)
        print(taskCounter)
        maxheap = [-task for task in taskCounter.values()]
        heapq.heapify(maxheap)
        
        queue = deque()
        time = 0

        while maxheap or queue:
            time += 1
            if not maxheap:
                time = queue[0][1]
            else:
                count = 1 + heapq.heappop(maxheap)
                if count:
                    queue.append((count, time+n))

            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue.popleft()[0])

        return time
