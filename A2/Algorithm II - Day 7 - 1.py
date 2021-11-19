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
        if not root:
            return root
        
        nodeList = self.bfs(root)    
        self.set_right_pointer(nodeList)
        return root
    
    def bfs(self, root):
        queue, nodeList = [], []
        queue.append(root)
        while queue:
            numberOfNodes = len(queue)
            nodes = []
            for i in range(numberOfNodes):
                node = queue.pop(0)
                nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            nodeList.append(nodes)
        return nodeList
    
    def set_right_pointer(self, nodeList):
        for nodes in nodeList:
            for i,node in enumerate(nodes):
                if i == len(nodes) - 1:
                    node.next = None
                else:
                    node.next = nodes[i+1] 