# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p1 = head
        p2 = head.next
        p3 = self.swapPairs(head.next.next)
        p2.next = p1
        p1.next = p3
        return p2
