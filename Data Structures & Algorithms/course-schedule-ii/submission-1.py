class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        adjlist => defaultdict(list)
        - b -> a
        adjlist[a].append(b) -> list of a's preqs
        for i in numCourses:
        '''
        result = []
        # seen, cycle = set(), set()
        adjlist = {i: [] for i in range(numCourses)}
        prereqs = [0] * numCourses

        for course, preq in prerequisites:
            adjlist[preq].append(course) #preq: courses
            prereqs[course] += 1

        queue = deque()
        for i in range(numCourses):
            if prereqs[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            result.append(course)
            for prereq in adjlist[course]:
                prereqs[prereq] -= 1
                if prereqs[prereq] == 0:
                    queue.append(prereq)

        if len(result) == numCourses:
            return result
        return []