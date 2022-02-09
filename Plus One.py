class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = 1
        while i > 0:
            if digits[n - i] == 9:
                digits[n - i] = 0
                i = i + 1
                if i == len(digits) + 1:
                    digits.insert(0, 1)
                    break
            else:
                digits[n - i] = digits[n - i] + 1
                break
        return digits