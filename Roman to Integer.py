class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in roman:
                res = res + roman[s[i:i+2]]
                i=i+2
            else:
                res = res + roman[s[i]]
                i=i+1
        return res