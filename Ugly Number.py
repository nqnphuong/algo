class Solution:
    def isUgly(self, n: int) -> bool:
        ugly = [2, 3, 5, 7]
        i = 0
        if n <= 0: return False
        while n > 1 and i != 3:
            print(n, ugly[i])
            if n % ugly[i] != 0:
                i += 1
            else:
                n = n // ugly[i]
        if i == 3: return False
        return True
