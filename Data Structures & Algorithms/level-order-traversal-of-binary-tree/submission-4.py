# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        if not root:
            return levels
        
        queue = deque([root]) #using a queue => bfs, start w root
        while queue: #root
            level = []
            for _ in range(len(queue)): #len queue = 1
                node = queue.popleft() #node = root, queue is empty
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            levels.append(level)

        return levels