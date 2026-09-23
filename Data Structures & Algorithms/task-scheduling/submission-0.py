class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        need to run the most frequent tasks at a given time
            - maxheap
            - pop from heap
        after popped, if still occurences left, add to queue
            - curr + n time
        '''
        taskCount = {task: 0 for task in tasks}
        for task in tasks:
            taskCount[task] += 1

        maxheap = [-task for task in taskCount.values()]
        heapq.heapify(maxheap)
        queue = deque() #remainingcountafterrunning, availablenext
        time = 0 #queue cycle

        while maxheap or queue:
            time += 1
            if not maxheap:
                time = queue[0][1]
            else:
                count = 1 + heapq.heappop(maxheap)
                if count:
                    queue.append([count, time+n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue.popleft()[0]) 
                
        return time