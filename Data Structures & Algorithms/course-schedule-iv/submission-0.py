class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        isPrereq = [set() for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adjList[pre].append(crs) #a is one of preq for b
            indegrees[crs] += 1

        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])

        while queue:
            node = queue.popleft()
            for nei in adjList[node]:
                isPrereq[nei].add(node) #if not there, add
                isPrereq[nei].update(isPrereq[node]) #if there, update
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        
        answer = []
        for u, v in queries:
            answer.append(u in isPrereq[v])

        return answer
