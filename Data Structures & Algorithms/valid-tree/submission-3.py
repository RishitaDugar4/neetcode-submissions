class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False #early exit

        adj = [[] for _ in range(n)]
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        visited = set() 
        def dfs(node, prev):
            if node in visited:
                return False #cycle?

            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue #the node u js came from
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
        