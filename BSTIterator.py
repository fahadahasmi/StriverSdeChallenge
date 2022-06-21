# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    st = []

    def __init__(self, root: Optional[TreeNode]):
        while root:
            self.st.append(root)
            root = root.left
        

    def next(self) -> int:
        node = self.st.pop()
        while node.right:
            self.st.append(node.right)
            node.right = node.right.left

        return node.val
        
        

    def hasNext(self) -> bool:
        return not (len(self.st)==0)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
