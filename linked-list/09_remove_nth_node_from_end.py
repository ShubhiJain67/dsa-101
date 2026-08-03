# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # return self.twoPass(head, n)
        return self.onePass(head, n)
    
    def onePass(self, head, n):
        slow = head
        fast = head.next
        n -= 1
        while n > 0:
            fast = fast.next
            n -= 1
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        if slow == None:
            return head
        elif prev == None:
            return head.next
        else:
            temp = slow.next
            slow.next = None
            prev.next = temp
        return head


    def twoPass(self, head, n):
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
