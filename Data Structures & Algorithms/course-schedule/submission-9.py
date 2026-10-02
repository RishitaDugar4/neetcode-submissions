class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        reqs = [0] * numCourses
        for src, dest in prerequisites:
            adjList[src].append(dest)
            reqs[dest] += 1 # indegree of dest

        queue = deque()
        for i, req in enumerate(reqs): #course, indegree
            if req == 0:
                queue.append(i) #course

        finished = 0
        while queue:
            for _ in range(len(queue)):
                taken = queue.popleft()
                finished += 1
                for neigh in adjList[taken]:
                    reqs[neigh] -= 1
                    if reqs[neigh] == 0:
                        queue.append(neigh)

        return finished == numCourses
