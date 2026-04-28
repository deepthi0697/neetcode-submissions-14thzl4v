# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        if p.val != q.val or p.left and not q.left or not p.left and q.left or not p.right and q.right or p.right and not q.right:
            return False
        
        
        if p.left and q.left:
            return self.isSameTree(p.left,q.left)
        
        if p.right and q.right:
            return self.isSameTree(p.right, q.right)
        
        return True