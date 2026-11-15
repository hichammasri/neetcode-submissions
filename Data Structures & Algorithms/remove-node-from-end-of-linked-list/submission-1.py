# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) ->Optional[ListNode]:
        if not (head and head.next):
            return None
        node = head
        futureNode = head
        for i in range(n):
            futureNode = futureNode.next
        if not futureNode:
            return node.next
        
        while futureNode.next:
            node = node.next
            futureNode = futureNode.next
        node.next = node.next.next

        return head

        

        