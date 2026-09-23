class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        build graph
        everytime you see a new component, (not connected to a seen edge)
            increment
            dfs
        '''
        components = 0
        seen = [False] * n
        graph = {i: [] for i in range(n)}
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        def bfs(node):
            queue = deque([node])
            seen[node] = True

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not seen[neighbor]:
                        seen[neighbor] = True
                        queue.append(neighbor)
        
        for i in range(n):
            if not seen[i]:
                bfs(i)
                components += 1

        return components

        