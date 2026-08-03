# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sizeA = self.getSize(headA)
        sizeB = self.getSize(headB)
        if sizeA < sizeB:
            headA, headB = headB, headA
        diff = abs(sizeA - sizeB)
        p1 = headA
        p2 = headB
        while diff > 0:
            p1 = p1.next
            diff -= 1
        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        if p1 != None and p1 == p2:
            return p1
        return None
    
    def getSize(self, head):
        size = 0
        while head:
            head = head.next
            size += 1
        return size
