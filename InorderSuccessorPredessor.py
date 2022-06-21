'''
    ------- Binary Tree node structure -------
            class   BinaryTreeNode :
                def __init__(self, data) :
                    self.data = data
                    self.left = None
                    self.right = None

                def __del__(self):
                    if self.left:
                        del self.left
                    if self.right:
                        del self.right
      
'''
def pred(root,key):
    node = -1
    while root:
        if root.data<key:
            node = root.data
            root = root.right
        else:
            root = root.left
    return node
def succ(root,key):
    node = -1
    while root:
        if root.data<=key:
            root = root.right
        else:
            node = root.data
            root = root.left
    return node

def predecessorSuccessor(root, key):
    
    pre = pred(root,key)
    suc = succ(root,key)
    return [pre,suc]
