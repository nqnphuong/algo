class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #islower(): kiem tra chu thuong chu hoa
        if word.islower() == True or word.isupper() == True or word.istitle() == True: return True
        else: return False
