# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        bfsP = []
        bfsQ = []

        def bfs(root, queue):
            if not root:
                queue.append(None)
                return

            queue.append(root.val)
            bfs(root.left, queue)
            bfs(root.right, queue)

            return queue
            
        return bfs(p, bfsP) == bfs(q, bfsQ)




        