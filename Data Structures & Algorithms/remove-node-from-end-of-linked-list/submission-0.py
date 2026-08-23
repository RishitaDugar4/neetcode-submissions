# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr != None:
            nodes.append(curr)
            curr = curr.next

        removal = len(nodes) - n
        
        if removal == 0:
            return head.next

        nodes[removal-1].next = nodes[removal].next
        return head