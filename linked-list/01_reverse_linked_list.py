# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p1 = head
        p2 = head.next
        while p2 is not None:
            p3 = p2.next
            p2.next = p1
            if p1 == head:
                p1.next = None
            p1 = p2
            p2 = p3
        return p1
