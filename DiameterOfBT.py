# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans = []
        
        def helper(r):
            if not r:
                return 0
            
            lh = helper(r.left)
            rh = helper(r.right)
            ans.append(lh+rh)
            
            return 1+max(lh,rh)
        
        a = helper(root)
        if not ans:
            return 0
        return max(ans)
            
