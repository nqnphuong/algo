class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = [0]+nums
        for i in range(3,len(nums)):
            nums[i]+=max(nums[i-3],nums[i-2])
        return max(nums[-1],nums[-2])