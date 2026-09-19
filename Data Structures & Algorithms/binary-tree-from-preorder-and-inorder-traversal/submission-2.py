# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        inorder: pre -> root -> post
            - mid tells us root
            - pre tells us left subtree
            - post tells us right subtree
        preorder: root -> pre -> post
            - tells us root
        '''
        if not preorder or not inorder:
            return None

        self.index = 0
        hashmap = {val: i for i, val in enumerate(inorder)}
        
        def dfs(left, right):
            if left > right:
                return None

            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(val=root_val)
            mid = hashmap[root_val]

            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)
            return root

        return dfs(0, len(inorder)-1)