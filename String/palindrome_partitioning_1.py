from typing import List

# https://leetcode.com/problems/palindrome-partitioning/


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def valid_palindrome(s, start, end):
            lp, rp = start, end
            while lp <= rp:
                if s[lp] != s[rp]:
                    return False
                lp += 1
                rp -= 1
            return True

        def solve(s, idx, ls):

            if idx == n:
                self.res.append(ls.copy())

            for i in range(idx, n):
                if valid_palindrome(s, idx, i):
                    ls.append(s[idx : i + 1])
                    solve(s, i + 1, ls)
                    ls.pop()

        self.res = []
        n = len(s)
        solve(s, 0, [])
        return self.res
