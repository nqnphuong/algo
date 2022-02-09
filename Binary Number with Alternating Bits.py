class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = []

        while n > 0:
            b.append(int(n % 2))
            n = int(n / 2)
        for j in range(len(b) - 1):
            if b[j] == b[j + 1]:
                return False
        return True
