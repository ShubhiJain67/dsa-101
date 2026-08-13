# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newHead = None
        head = None
        while l1 or l2 or carry:
            if l1 and l2:
                currSum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                currSum = l1.val + carry
                l1 = l1.next
            elif l2:
                currSum = l2.val + carry
                l2 = l2.next
            else:
                currSum = carry
            currVal = currSum % 10
            carry = int(currSum / 10)
            newNode = ListNode(currVal)
            if newHead == None:
                newHead = newNode
            if head != None:
                head.next = newNode
            head = newNode
        return newHead
