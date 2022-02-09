class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        up = 0
        down = 0
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                up = up + 1
            if nums[i] >= nums[i + 1]:
                down = down + 1
        if up == len(nums) - 1 or down == len(nums)-1: return True
        else: return False