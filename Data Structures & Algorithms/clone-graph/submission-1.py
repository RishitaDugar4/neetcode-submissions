"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hashmap = {} # {}
        
        # deep copies of every node
        def dfs(node):
            if node in hashmap:
                return
            else:
                hashmap[node] = Node(node.val) # deep copy

            for n in node.neighbors:
                # N1: Node(1) = []
                dfs(n)
                hashmap[node].neighbors.append(hashmap[n])

        # populate hashmap
        dfs(node)

        return hashmap[node]

        
        