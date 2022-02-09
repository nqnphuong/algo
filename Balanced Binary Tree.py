# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.trans(root)[0]

    def trans(self, root):
        if not root: return True, 0
        left, leftD = self.trans(root.left)
        right, rightD = self.trans(root.right)
        res = left and right and abs(leftD - rightD) <= 1
        depth = max(leftD, rightD) + 1
        return res, depth