class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = format(x, '0200b')
        lst1 = list(a)
        b = format(y, '0200b')
        lst2 = list(b)
        res = 0
        for i in range(200):
            if lst1[i] != lst2[i]: res = res + 1
        return(res)