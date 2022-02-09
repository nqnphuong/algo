class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1: return True
        su = 10
        while su>9:
            su = 0
            while n>0:
                su = su + pow(n%10,2)
                n = n//10
            if su == 1 or su == 7: return True
            else: n = su
        return False