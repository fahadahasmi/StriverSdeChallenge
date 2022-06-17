from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        ans = 0
        q = deque()
        q.append((root, 0))
        while q:
            size = len(q)
            curMin = q[0][1]
            leftMost, rightMost = 0, 0
            for i in range(size):
                cur_id = q[0][1] - curMin
                node = q.popleft()[0]
                if i == 0:
                    leftMost = cur_id
                if i == size - 1:
                    rightMost = cur_id
                if node.left:
                    q.append((node.left, cur_id * 2 + 1))
                if node.right:
                    q.append((node.right, cur_id * 2 + 2))
            ans = max(ans, rightMost - leftMost + 1)
        return ans
