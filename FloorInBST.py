def floorInBST(root, X):
    floor = -1
    while root:
        if root.data == X:
            floor = root.data
            return floor
        if X > root.data:
            floor = root.data
            root = root.right
        else:
            root = root.left
    return floor
