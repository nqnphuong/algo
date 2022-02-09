class Solution:
    def reverse(self, x: int) -> int:
        lst = list(str(x))
        lst.reverse()
        if lst[len(lst)-1] == '-':
            lst.remove('-')
            res = int("".join(lst))*-1
        else:
            res = int("".join(lst))
        if res >= pow(2,31)-1 or res <= -pow(2,31): return 0
        return res