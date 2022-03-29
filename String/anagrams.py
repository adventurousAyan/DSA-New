from typing import List

# Brute Force


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        lp = 0
        rp = lp + n - 1
        ls = []
        while lp <= rp and rp <= len(s) - 1:
            s1 = s[lp : rp + 1]
            if sorted(s1) == sorted(p):
                ls.append(lp)
            lp = lp + 1
            rp = rp + 1
        return ls
