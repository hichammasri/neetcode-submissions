# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not (head and head.next):
            print('hi')
            print(head.val) if head else None
            return

        node = head
        while node.next and node.next.next:
            node = node.next
        beforeTail = node
        tail = node.next

        beforeTail.next = None
        tail.next = head.next
        head.next = tail
        
        self.reorderList(tail.next)

        