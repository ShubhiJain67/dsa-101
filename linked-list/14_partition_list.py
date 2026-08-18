# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        newHead = None
        left = None
        right = None
        prev = None
        while head is not None:
            node = head
            head = head.next
            node.next = None
            if newHead is None and right is None and left is None:
                # print(f"Inserting first node {node.val}")
                newHead = node
                right = node
                if node.val < x:
                    left = node
            elif node.val < x:
                if left is None:
                    # print(f"Inserting first left {node.val}")
                    node.next = newHead
                    left = node
                    newHead = left
                else:
                    # print(f"Inserting left {node.val}")
                    temp = left.next
                    left.next = node
                    node.next = temp
                    if right == left:
                        right = right.next
                    left = left.next
            else:
                # print(f"Inserting right {node.val}")
                right.next = node
                right = right.next
            # self.printList(newHead)
        return newHead

    # def printList(self, node):
    #     while node:
    #         print(f"{node.val} ->", end = "")
    #         node = node.next
    #     print()
