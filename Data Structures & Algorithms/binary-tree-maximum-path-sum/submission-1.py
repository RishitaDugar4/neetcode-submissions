# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftmax = max(0, dfs(root.left))
            rightmax = max(0, dfs(root.right))

            result[0] = max(result[0], root.val+leftmax+rightmax)
            return root.val + max(leftmax, rightmax)

        dfs(root)
        return result[0]