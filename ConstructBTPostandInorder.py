# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(inorder,inS,inE,postorder,pS,pE,mp):
    if inS>inE or pS>pE:
        return None
    
    root = TreeNode(postorder[pE])
    elem = mp[root.val]
    nL = elem-inS
    root.left = helper(inorder,inS,elem-1,postorder,pS,pS+nL-1,mp)
    root.right = helper(inorder,elem+1,inE,postorder,pS+nL,pE-1,mp)
    return root

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d = defaultdict(int)
        
        for i in range(len(inorder)):
            d[inorder[i]] = i
        
        root = helper(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1,d)
        return root
        
