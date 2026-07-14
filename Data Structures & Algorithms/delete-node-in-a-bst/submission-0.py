# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minVal (self, root):
        curr = root
        while curr and curr.left: #leftmost node
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: #once you traversed tree to find node
            #if cases to handle 0-1 children --> 0 children = base case
            # 1 children handled here => return the leg with the children
            if not root.left: 
                return root.right
            elif not root.right:
                return root.left
            else: #two leg case
                minNode = self.minVal(root.right) #right subtree --> find leftmost node in right subtree = find successor
                root.val = minNode.val #swap successor and deleted; root is deleted
                root.right = self.deleteNode(root.right, minNode.val)
        return root