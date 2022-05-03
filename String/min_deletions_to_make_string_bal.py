class Solution:
    # https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
    def minimumDeletions(self, s: str) -> int:

        prefix = 0
        total = 0
        for i in range(0, len(s)):
            if s[i] == "a" and prefix > 0:
                prefix -= 1
                total += 1
            if s[i] == "b":
                prefix += 1
        return total
