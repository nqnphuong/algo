class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m = len(nums)
        list = []
        for i in range(1, m + 1):
            list.append(i)
        return set(nums).symmetric_difference(set(list))
