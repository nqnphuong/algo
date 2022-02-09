class Solution:
    def firstUniqChar(self, s: str) -> int:
        lst = list(s)
        res = [k for k, v in collections.Counter(lst).items() if v == 1]
        if not res: return -1
        for i in range(len(lst)):
            if res[0] == lst[i]:
                return i