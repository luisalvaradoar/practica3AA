class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        frontend = backend = head
        for length in range(0, n):
            frontend = frontend.next
        if frontend is None:
            return head.next
        while frontend.next is not None:
            backend = backend.next
            frontend = frontend.next
        backend.next = backend.next.next

        return head