# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(arr,bound):
    
    if not arr or arr[-1]>bound: 
        return None
    
    root = TreeNode(arr.pop())
    root.left = helper(arr,root.val)
    root.right = helper(arr,bound)
    return root

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        bound = float("inf")
        preorder = preorder[::-1]
        return helper(preorder,bound)
    
