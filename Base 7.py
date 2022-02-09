class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        big = 1
        if num < 0:
            big = -1
            num = -1*num
        res = ''
        while num>0:
            res = str(num%7) + res
            num = num //7
        return ('-' if big < 0 else '') + res