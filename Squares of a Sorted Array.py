class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res.append(i * i)
        # for i in range(1,len(res)):
        #     key = res[i]
        #     j = i-1
        #     while j >= 0 and res[j] > key:
        #         res[j+1] = res[j]
        #         j = j-1
        #     res[j+1] = key
        return sorted(res)

