# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    flag = False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root and self.flag == False:
                     
            if root.val == subRoot.val:
                if self.check(root,subRoot): self.flag = True        
                           
            self.isSubtree(root.left, subRoot)
            self.isSubtree(root.right, subRoot)
                        
        return self.flag
    
    
    def check(self,root,subroot):
        
        if not root and not subroot:
            return True
        
        if (not root and subroot) or (root and not subroot):
            return False
        
        if root.val != subroot.val:
            return False
        
        return self.check(root.left, subroot.left) and self.check(root.right, subroot.right)