# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        fast = head
        slow = head
        prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        result = self.merge(left, right)
        return result
    
    def merge(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        if left.val <= right.val:
            node = left
            left = left.next
        else:
            node = right
            right = right.next
        node.next = None
        node.next = self.merge(left, right)
        return node
        
        
