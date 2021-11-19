class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        head  = dummy
            
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next  	
        if l1:
            head.next = l1
        elif l2:
            head.next = l2
            
        return dummy.next