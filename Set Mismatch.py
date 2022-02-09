class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = sum(set(nums))
        dup = sum(nums) - res
        miss = (len(nums) + 1) * len(nums) // 2 - res
        return [dup, miss]
