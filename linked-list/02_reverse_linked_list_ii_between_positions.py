class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        distance = right - left

        prev = None
        p1 = head

        while left > 1:
            prev = p1
            p1 = p1.next
            left -= 1

        p2 = p1

        while distance > 0:
            p2 = p2.next
            distance -= 1

        after = p2.next
        p2.next = None

        revStart, revEnd = self.reverseList(p1)

        if prev:
            prev.next = revStart
        else:
            head = revStart

        revEnd.next = after

        return head

    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev, head
