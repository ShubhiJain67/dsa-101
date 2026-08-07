from typing import List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.merge(lists, 0, len(lists)-1)

    def merge(self, lists, start, end):
        if not lists or start > end:
            return None
        if start == end:
            return lists[start]
        listLen = start + (end - start)//2
        leftMerge = self.merge(lists, start, listLen)
        rightMerge = self.merge(lists, listLen+1, end)
        # return self.merge2SortedListsOutPlace(leftMerge, rightMerge)
        # return self.merge2SortedListsInPlace(leftMerge, rightMerge)
        return self.merge2Optimised(leftMerge, rightMerge)
    
    def merge2Optimised(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.merge2Optimised(list1.next, list2)
            return list1
        else:
            list2.next = self.merge2Optimised(list1, list2.next)
            return list2

    def merge2SortedListsInPlace(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        head = list1
        while list1 and list2:
            prev = None
            while list1 and list1.val <= list2.val:
                prev = list1
                list1 = list1.next
            prev.next = list2
            list1, list2 = list2, list1

        return head
        
        
    def merge2SortedListsOutPlace(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        p1 = list1
        p2 = list2
        p3 = None
        newHead = None
        while p1 and p2:
            if p1.val < p2.val:
                newNode = ListNode(p1.val, None)
                p1 = p1.next
            else:
                newNode = ListNode(p2.val, None)
                p2 = p2.next
            if not newHead:
                newHead = newNode
            if not p3:
                p3 = newNode
            else:
                p3.next = newNode
                p3 = p3.next
        if p1:
            p3.next = p1
        if p2:
            p3.next = p2
        return newHead
        
