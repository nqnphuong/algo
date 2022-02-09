class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/
        left, right = 0, sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if left == right: return i
            left += nums[i]
        return -1