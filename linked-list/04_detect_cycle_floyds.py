# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return bool(self.floyd(head))

    # Cannot be used for cycle detection
    def shiftedFloyd(self, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not slow or not slow.next or not fast or not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
    
    # Good fo cycle detection
    def floyd(self, head):
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        return True
