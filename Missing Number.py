class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        for i in range(n):
            if i != nums[i]:
                # nums.insert(i,i)
                return i
        # nums.append(n)
        return n
