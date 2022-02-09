class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        lst = list(columnTitle)
        sum = 0
        n = len(lst)
        for i in range(0,n):
            #vt la so vi tri cua ki tu do: A = 1, B = 2
            vt = ord(lst[i]) - 64
            sum = sum + pow(26,n-i-1)*vt
        return(sum)