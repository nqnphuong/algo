# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sumOfLeft(root, flag):
            if not root: return 0
            if flag and not root.left and not root.right:
                return root.val
            return sumOfLeft(root.left, True) + sumOfLeft(root.right, False)

        return sumOfLeft(root, False)
