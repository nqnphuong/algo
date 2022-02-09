# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        lit = []

        def trans(root: Optional[TreeNode]):
            if not root: return -1
            trans(root.left)
            lit.append(root.val)
            trans(root.right)

        trans(root)
        res = sorted(set(lit))
        if len(res) >= 2:
            return res[1]
        return -1
