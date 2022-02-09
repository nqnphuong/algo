class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lit = list(s)
        for i in range(0, len(s), 2 * k):
            lit[i:i + k] = lit[i:i + k][::-1]
        return "".join(lit)
