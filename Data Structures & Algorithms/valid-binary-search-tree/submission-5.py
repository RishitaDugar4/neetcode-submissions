# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        #node, lower, upper
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            for _ in range(len(queue)):
                node, lower, upper = queue.popleft()

                if not (lower < node.val < upper):
                    return False

                if node.left:
                    queue.append((node.left, lower, node.val))

                if node.right:
                    queue.append((node.right, node.val, upper))

        return True
        