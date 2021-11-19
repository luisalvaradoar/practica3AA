# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = head
        l = 1
        while(b.next!=None):
            b = b.next
            l += 1
        c = 1
        while(c < int(l/2)+1):
            a = a.next
            c += 1
        return a