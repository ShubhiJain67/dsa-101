# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head1 = head
        head2 = head.next
        list1 = head
        list2 = head.next
        head = head.next.next
        list1.next = None
        list2.next = None
        first = True
        while head:
            if first:
                list1.next = head
                head = head.next
                list1 = list1.next
                list1.next = None
            else:
                list2.next = head
                head = head.next
                list2 = list2.next
                list2.next = None
            first = not first
        list1.next = head2
        return head1
