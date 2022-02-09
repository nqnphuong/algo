class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            res = True
            if bits[i] == 1:
                i = i + 2
                res = False
            else:
                i = i + 1
        return res

