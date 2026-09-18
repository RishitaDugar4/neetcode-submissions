# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, maxonpath):
            if not node:
                return 0

            if node.val >= maxonpath:
                maxonpath = max(maxonpath, node.val)
                result = 1
            else:
                result = 0

            result += dfs(node.left, maxonpath)
            result += dfs(node.right, maxonpath)

            return result

        return dfs(root, root.val)
