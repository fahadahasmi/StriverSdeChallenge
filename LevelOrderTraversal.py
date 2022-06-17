# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = []
        
        q.append(root)
        
        while len(q) > 0:
            l = []
            for i in range(len(q)):
                node = q.pop(0)
                l.append(node.val)
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)
            ans.append(l)
        
        return ans
            
