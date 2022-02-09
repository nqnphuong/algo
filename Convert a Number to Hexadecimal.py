class Solution:
    def toHex(self, num: int) -> str:
        hexa = "0123456789abcdef"
        res = []
        if not num :
            return "0"
        while num and len(res) != 8:
            n = num & 15
            res.append(hexa[n])
            num >>= 4

        return ''.join(res[::-1])