class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while True:
            if pow(2, i) == n: return True
            if pow(2, i) > n: return False
            i = i + 1
