'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def findCeil(root, x):
    ceil = -1
    while root:
        if root.data ==x:
            ceil = root.data
            return ceil
        if x > root.data:
            root = root.right
        else:
            ceil = root.data
            root = root.left
    return ceil
