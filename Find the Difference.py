class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lst = list(t) + list(s)
        res = [k for k, v in collections.Counter(lst).items() if v % 2 == 1]
        return ("".join(res))
