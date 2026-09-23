class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        adjlist => defaultdict(list)
        - b -> a
        adjlist[a].append(b) -> list of a's preqs
        for i in numCourses:
        '''
        result = []
        seen, cycle = set(), set()
        adjlist = defaultdict(list)

        for course, preq in prerequisites:
            adjlist[course].append(preq)

        def dfs(course):
            if course in cycle:
                return False
            if course in seen:
                return True
            
            cycle.add(course)
            for preq in adjlist[course]:
                if dfs(preq) == False:
                    return False

            cycle.remove(course)
            seen.add(course)
            result.append(course)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return result