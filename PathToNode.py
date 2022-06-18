# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        if A is None:
            return ans
        
        def helper(root):
            if root is None:
                return False
            
            ans.append(root.val)
            if root.val==B:
                return True
            if helper(root.left) or helper(root.right):
                return True
            ans.pop()
            return False
              
        
        helper(A)
        return ans
