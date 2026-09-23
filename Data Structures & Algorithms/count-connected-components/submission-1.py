class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        build graph
        everytime you see a new component, (not connected to a seen edge)
            increment
            dfs
        '''
        components = 0
        seen = set()
        graph = {i: [] for i in range(n)}
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        def dfs(node):
            if node in seen:
                return

            seen.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        for i in range(n):
            if i not in seen:
                dfs(i)
                components += 1

        return components

        