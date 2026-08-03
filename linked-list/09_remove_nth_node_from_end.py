# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        positonToDelete = self.getLen(head) - n
        while positonToDelete>0 and curr:
            prev = curr
            curr = curr.next
            positonToDelete -= 1
        if curr == None:
            return head
        if prev == None:
            return head.next
        if positonToDelete == 0:
            temp = curr.next
            curr.next = None
            prev.next = temp
        return head
    
    def getLen(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size
