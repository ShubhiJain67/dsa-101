# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # return self.extraSpace(head)
        return self.constantSpace(head)

    def constantSpace(self, head):
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if fast:
            second = slow.next
            slow.next = None
        else:
            second = slow
            prev.next = None
        second = self.reverseList(second)
        first = head
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def extraSpace(self, head):
        store = []
        while head:
            store.append(head.val)
            head = head.next
        i = 0
        j = len(store) - 1
        while i < j:
            if store[i] != store[j]:
                return False
            i += 1
            j -= 1

        return True
