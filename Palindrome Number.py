class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = list(str(x))
        for i in range(int(len(lst) / 2)):
            if lst[i] != lst[len(lst) - 1 - i]: return False
        return True
