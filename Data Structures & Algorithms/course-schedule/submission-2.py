class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        need b to take a: b -> a
        adjList, implemented w hashmap
        '''
        queue = deque()
        adjList = collections.defaultdict(list)
        indegree = [0] * numCourses
        takenCourses = 0

        for preq in prerequisites:
            src, dest = preq[1], preq[0]
            if src not in adjList:
                adjList[src] = []

            if dest not in adjList:
                adjList[dest] = []

            adjList[src].append(dest)
            indegree[dest] += 1
            
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i) #courses are numbered

        while queue:
            course = queue.popleft()
            takenCourses +=1 
            
            for neighbor in adjList[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)


        return takenCourses == numCourses

        
