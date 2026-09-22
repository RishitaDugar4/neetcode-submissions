class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for crs, preq in prerequisites:
            adj[crs].append(preq) #need to take all dest before src

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False #cycle

            if adj[crs] == []:
                return True

            visited.add(crs)
            for prereq in adj[crs]:
                if not dfs(prereq):
                    return False
            visited.remove(crs)
            adj[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True