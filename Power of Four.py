class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        while True:
            if pow(4,i) == n: return True
            if pow(4,i) > n: return False
            i = i + 1