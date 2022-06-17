# Following is the Binary Tree node structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isleaf(root):
    return (not root.left) and (not root.right)

def left(root,res):
    cur = root.left
    while cur:
        if isleaf(cur) == False:
            res.append(cur.data)
        if cur.left:
            cur = cur.left
        else:
            cur = cur.right

def leaf(root,res):
    if isleaf(root):
        res.append(root.data)
        return
    if root.left:
        leaf(root.left,res)
    if root.right:
        leaf(root.right,res)

def right(root,res):
    temp =[]
    cur = root.right
    while cur:
        if isleaf(cur) == False:
            temp.append(cur.data)
        if cur.right:
            cur = cur.right
        else:
            cur= cur.left
    for i in range(len(temp)-1,-1,-1):
        res.append(temp[i])

def traverseBoundary(root):
    # Write your code here.
    res = []
    if not root:
        return res
    if isleaf(root)==False:
        res.append(root.data)
    left(root,res)
    leaf(root,res)
    right(root,res)
    return res
