class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n-1:
            if nums[i] == nums[i+1]:
                del nums[i + 1]
                n = len(nums)
            else: i = i + 1
        return n