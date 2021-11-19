"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
		# The root type annotation is wrong (should be Optional[Node]).
		# Hence, we also need to check that root is not None.
        if not root or not root.left:
            return root

        root.left.next = root.right
        root.left = self.connect(root.left)
        root.right.next = root.next and root.next.left 
        root.right = self.connect(root.right)
        return root