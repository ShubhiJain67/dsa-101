# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        return self.reverse(head, k, length)

    def reverse(self, head, k, currLen):
        if currLen < k:
            return head

        prev = None
        curr = head

        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head.next = self.reverse(curr, k, currLen - k)

        return prev
