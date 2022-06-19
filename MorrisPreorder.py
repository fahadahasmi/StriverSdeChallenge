# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur = root
        while cur:
            if not cur.left:
                ans.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right is not cur:
                    pre = pre.right
                
                if pre.right:
                    pre.right = None
                    cur = cur.right
                else:
                    pre.right = cur
                    ans.append(cur.val)
                    cur = cur.left
                
        
        return ans
        
