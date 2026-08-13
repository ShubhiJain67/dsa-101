# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.getLength(head)
        if n < 2:
            return head
        k = k % n
        slow = head
        fast = head
        while fast and k > 0:
            fast = fast.next
            k -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        newHead = slow.next
        slow.next = None
        temp = newHead
        if not temp:
            return head
        while temp and temp.next:
            temp = temp.next
        temp.next = head
        return newHead
    
    def getLength(self, head):
        n = 0
        while head:
            n += 1
            head = head.next
        return n

