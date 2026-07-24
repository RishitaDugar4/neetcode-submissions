# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxDepth = 0

        bfs = deque([root])

        while bfs:
            for _ in range(len(bfs)):
                node = bfs.popleft()

                if node.left:
                    bfs.append(node.left)

                if node.right:
                    bfs.append(node.right)
            
            maxDepth += 1

        return maxDepth

            




        


        