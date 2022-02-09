# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def trans(root):
            if not root: return 0
            left = trans(root.left)
            right = trans(root.right)
            self.res = self.res + abs(left - right)
            return left + right + root.val

        self.res = 0
        trans(root)
        return self.res