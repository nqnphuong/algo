class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = int(num1)
        m = int(num2)
        return "".join(str(n + m))
