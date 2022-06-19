# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(preorder,preS,preE,inorder,inS,inE,mp):
    if preS> preE or inS > inE:
        return None
    
    root = TreeNode(preorder[preS])
    elem = mp[root.val]
    nextELe = elem - inS
    root.left = helper(preorder,preS+1,preE+nextELe,inorder,inS,elem-1,mp)
    root.right = helper(preorder,preS+nextELe+1,preE,inorder,elem+1,inE,mp)
    return root
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = defaultdict(int)
        for i in range(len(inorder)):
            d[inorder[i]] = i
        
        root = helper(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,d)
        return root
        
