# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float("-inf")
        def helper(root):
            nonlocal maxi
            if not root:
                return 0

            l = max(0,helper(root.left))
            r = max(0,helper(root.right))
            maxi = max(maxi,l+r+root.val)

            return root.val+max(l,r)
        
        helper(root)
        return maxi
        
        
