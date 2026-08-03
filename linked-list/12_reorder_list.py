# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        headA, headB = self.getHeads(head)
        reverseHeadB = self.reverse(headB)
        self.merge(headA, reverseHeadB)
    
    def merge(self, headA, headB):
        if not headA:
            return headB
        if not headB:
            return headA
        rest = self.merge(headA.next, headB.next)
        headA.next = headB
        headB.next = rest
        return headA
    
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        nxt = head.next
        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
        curr.next = prev
        return curr


    def getHeads(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        newHead = slow.next
        slow.next = None
        return head, newHead
