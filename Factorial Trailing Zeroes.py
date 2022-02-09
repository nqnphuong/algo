class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 1
        count = 0
        for i in range(1,n+1):
            res = res*i
        # print(res)
        while res>0:
            if res % 10 == 0: count+=1
            else: break
            res = res // 10
        return count