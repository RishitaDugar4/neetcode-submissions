class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        reqs = [0] * numCourses

        for crs, preq in prerequisites:
            reqs[crs] += 1
            adj[preq].append(crs) #list of courses that depend on preq

        queue = deque() #bfs implementation

        for i, preq in enumerate(reqs):
            if preq == 0: #no more prereqs left, can take class
                queue.append(i)

        finished = 0 #class you've finished
        while queue: #classes to take
            taken = queue.popleft() 
            finished += 1
            for c in adj[taken]:
                reqs[c] -= 1
                if reqs[c] == 0:
                    queue.append(c)

        return finished == numCourses