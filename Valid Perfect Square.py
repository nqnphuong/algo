class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        if num == 1: return True
        while i*i <= num:
            if i*i == num: return True
            i += 1
        return False