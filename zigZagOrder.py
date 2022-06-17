# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        q = []
        q.append(root)
        t = 1
        while len(q)>0:
            r=[]
            for i in range(len(q)):
                node = q.pop(0)
                r.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(r[::t])
            t*=(-1)
        
        return ans
                
        
