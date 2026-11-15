# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) ->Optional[ListNode]:
    #     if not (head and head.next):
    #         return None
    #     node = head
    #     futureNode = head
    #     for i in range(n):
    #         futureNode = futureNode.next
    #     if not futureNode:
    #         return node.next
        
    #     while futureNode.next:
    #         node = node.next
    #         futureNode = futureNode.next
    #     node.next = node.next.next

    #     return head
    # def removeNthAndReportDecision(self, head: Optional[ListNode], n: int) ->None:
    #     if not head.next:
    #         if n == 1:
    #             return 1
    def removeNthOrReportPosition(self, head: Optional[ListNode], n:int) ->int:
        if not head.next:
            if n == 1:
                return 0, None
            return 0, head
        lastPos, lastHead = self.removeNthOrReportPosition(head.next, n)
        nextPos = 1 + lastPos
        if nextPos == n:
            head.next = head.next.next
        return nextPos, head

        
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) ->Optional[ListNode]:
        dummyNode = ListNode(0 ,head)
        return self.removeNthOrReportPosition(dummyNode, n)[1].next
        


        

        