# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = 0
        self.trans(root, low, high)
        return self.result

    def trans(self, root, low, high):
        if not root: return 0
        if root.val >= low and root.val <= high:
            self.result += root.val
        self.trans(root.left, low, high)
        self.trans(root.right, low, high)