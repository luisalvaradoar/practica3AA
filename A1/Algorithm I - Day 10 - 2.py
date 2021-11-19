# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        temp = head
        node_list = []
        
        while temp:
            node_list.append(temp)
            temp = temp.next
            
        node_list[0].next = None
        for idx, node in enumerate(node_list[1:]):
            node.next = node_list[idx]
        
        return node_list[-1]