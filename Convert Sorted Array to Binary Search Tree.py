# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return TreeNode()
        if len(nums) == 1: return TreeNode(nums[0])
        def BST(l: int, r: int) -> TreeNode:
            if l > r: return None
            m = l + (r - l) // 2
            root = TreeNode(nums[m])
            root.left = BST(l, m - 1)
            root.right = BST(m + 1, r)
            return root
        return BST(0, len(nums) - 1)