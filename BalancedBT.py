# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(r):
            if not r:
                return 0
            
            l = helper(r.left)
            if l==-1:
                return -1
            r = helper(r.right)
            if r==-1:
                return -1
            
            if abs(l-r)>1:
                return -1
            
            return 1+max(l,r)
        
        return helper(root) != -1
        
