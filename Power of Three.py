class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        while True:
            if pow(3,i) == n: return True
            if pow(3,i) > n: return False
            i = i + 1