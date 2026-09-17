"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: #has a value
            return None
        
        hashmap = {} # {N1 : Node(1), N2: Node(2): [Node(1)], N3: Node(3)}
        def dfs(node):
            if node in hashmap:
                return
            else:
                hashmap[node] = Node(node.val)

            for neighbor in node.neighbors:
                dfs(neighbor)
                hashmap[node].neighbors.append(hashmap[neighbor])
                # Node(2).neighbors = [Node(1), Node(3)]
                # Node(3).neighbors = [Node(2)]
                # Node(1).neighbors = [Node(2)]
    
        dfs(node)
        
        return hashmap[node]
        