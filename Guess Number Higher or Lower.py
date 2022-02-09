# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        while True:
            # n la high
            # l la low
            mid = ((n - l) // 2) + l
            if guess(mid) == 0: return mid
            if guess(mid) == -1:
                n = mid - 1
            if guess(mid) == 1:
                l = mid + 1
