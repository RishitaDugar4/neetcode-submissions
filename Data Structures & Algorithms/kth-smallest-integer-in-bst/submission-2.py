# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        queue = deque([root])
        bst = []
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                bst.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        bst.sort()
        print(bst)
        i = 1
        for idx in range(1, len(bst)+1):
            if i == k:
                return bst[i-1]
            i+=1
