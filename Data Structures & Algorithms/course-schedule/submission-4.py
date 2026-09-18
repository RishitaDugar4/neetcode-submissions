class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(numCourses)}
        visited = set()

        for crs, pre in prerequisites:
            adjList[crs].append(pre)


        def dfs(course):
            if course in visited:
                return False #return if cycle

            if adjList[course] == []:
                return True #reached a course w no preqs

            visited.add(course)
            for pre in adjList[course]:
                if not dfs(pre):
                    return False
            visited.remove(course) #backtracking
            adjList[course] = []

            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            


