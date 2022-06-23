'''

    ------- Binary Tree node structure -------
            class TreeNode :
                def __init__(self, data) :
                    self.data = data
                    self.left = None
                    self.right = None
    if root is None:
        return 0, 0, 0
    left_size, left_min, left_max = largestBST(root.left)
    right_size, right_min, right_max = largestBST(root.right)
    if left_max < root.data and right_min > root.data:
        return max(left_size, right_size) + 1, left_min, right_max
    else:
        return 0, 0, 0

'''
class Node: 
    def __init__(self, min, max, size, isBST):
        self.min = min
        self.max = max
        self.size = size
        self.isBST = isBST

def helper(root):
    if root is None:
        return Node(float("inf"), float("-inf"), 0, True)

    left = helper(root.left)
    right = helper(root.right)

    if left.isBST and right.isBST and (left.max < root.data < right.min):
        info = Node(min(root.data, min(left.min, right.min)),
                        max(root.data, max(left.max, right.max)),
                        left.size + 1 + right.size, True)
    else:
        info = Node(0, 0, max(left.size, right.size), False)

    return info

def largestBST(root):
    ans = helper(root)
    return ans.size
    
    
