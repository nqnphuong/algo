# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        res, q = [], [root]
        while q:
            val, cur = [], []
            for node in q:
                val.append(node.val)
                #duyet
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            res.append(val)
            q = cur
        return res[::-1]