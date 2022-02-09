# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #breadth-first search
        res = []
        queue = []
        queue.append(root)
        while queue:
            n = len(queue)
            step = []
            for i in range(n):
                node = queue.pop(0)
                step.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sum(step) / len(step))
        return res