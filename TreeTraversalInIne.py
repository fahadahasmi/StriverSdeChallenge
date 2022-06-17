# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def helper(r,inord,preord,postord):
    if not r:
        return 
    preord.append(r.data)
    helper(r.left,inord,preord,postord)
    inord.append(r.data)
    helper(r.right,inord,preord,postord)
    postord.append(r.data)
        
def getTreeTraversal(root):
    if not root:
        return [[],[],[]]
    inorder = []
    preorder = []
    postorder = []
    helper(root,inorder,preorder,postorder)
    return [inorder,preorder,postorder] 
        
