class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        dele = set()

        for char in s:
            if char in dele:
                pairs += 1
                dele.remove(char)
            else:
                dele.add(char)

        return pairs * 2 + 1 if dele else pairs * 2