# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:                                                                                     
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:                     
        p = head                                                                                    
        prev = None                                                                                 
        root = ListNode()                                                                           
        q = root                                                                                    
        while p is not None:                                                                        
            if (p.next is None or p.next.val != p.val) and (prev is None or prev.val != p.val):     
                q.next = p                                                                          
                q = q.next                                                                          
            prev = p                                                                                
            p = p.next                                                                              
        q.next = None                                                                               
        return root.next