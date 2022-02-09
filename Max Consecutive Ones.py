class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        count = 0
        for i in nums:
            if i == 1:
                count = count + 1
                res.append(count)
            else:
                count = 0
        return max(res, default=0)

