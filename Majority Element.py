class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = [k for k, v in collections.Counter(nums).items() if v > len(nums)/2]
        for i in res:
            return i