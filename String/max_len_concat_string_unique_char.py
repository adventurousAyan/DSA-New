from typing import List

# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        self.ans = 0
        return self.solve(arr, n, [], 0, "")

    def solve(self, arr, n, ls, j, s):
        if j == n:
            if self.isUnique(s):
                self.ans = max(len(s), self.ans)
            return
        else:
            ns = s + arr[j]
            if self.isUnique(ns):
                self.solve(arr, n, ls, j + 1, ns)
            self.solve(arr, n, ls, j + 1, s)
        return self.ans

    def isUnique(self, s):
        return len(s) == len(set(s))
