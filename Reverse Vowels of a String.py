class Solution:
    def reverseVowels(self, s: str) -> str:
        ngam = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        lit = list(s)
        i = 0
        j = len(lit)-1
        while i<j:
            print(i,j)
            if lit[i] in ngam and lit[j] in ngam:
                temp = lit[i]
                lit[i] = lit[j]
                lit[j] = temp
                i += 1
                j -= 1
            else:
                if lit[i] not in ngam: i += 1
                if lit[j] not in ngam: j -= 1
        return "".join(lit)