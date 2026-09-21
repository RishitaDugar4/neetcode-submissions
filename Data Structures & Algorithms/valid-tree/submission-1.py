class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False #early exit

        hashmap = defaultdict(list)
        for src, dest in edges:
            hashmap[src].append(dest)
            hashmap[dest].append(src)

        visited = set() 
        def dfs(node, par):
            if node in visited:
                return False #cycle?

            visited.add(node)
            for neighbor in hashmap[node]:
                if neighbor == par:
                    continue #the node u js came from
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
        