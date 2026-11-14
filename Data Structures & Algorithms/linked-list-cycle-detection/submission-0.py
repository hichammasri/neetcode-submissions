# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        node = head
        fasterNode = head

        while fasterNode and fasterNode.next:
            if fasterNode.next == node:
                return True
            fasterNode = fasterNode.next.next
            node = node.next
        
        return False
        