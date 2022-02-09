class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        cur = float("-inf")
        for i in nums:
            cur = max(cur+i, i)
            res = max(res, cur)
        return res