class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # dung dict
        s3 = s1 + " " + s2
        lst = s3.split()
        res = [k for k, v in collections.Counter(lst).items() if v == 1]
        return res

