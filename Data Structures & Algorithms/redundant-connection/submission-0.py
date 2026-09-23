class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges)+1)]

        def isCycle(node, prev):
            if node in seen:
                return True

            seen.add(node)
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if isCycle(neighbor, node):
                    return True
            return False

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
            seen = set()
            
            if isCycle(e1, -1):
                return [e1, e2]

        return []
        

        
        