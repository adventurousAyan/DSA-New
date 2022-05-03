from typing import List

# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        self.ans = 0
        ls = self.solve(arr, n, [], 0, "")
        if len(ls) > 0:
            return max([len(x) for x in ls])
        else:
            return 0

    def solve(self, arr, n, ls, j, s):
        if j == n:
            return
        else:
            for i in range(j, n):
                s += arr[i]
                if self.isUnique(s):
                    ls.append(s)
                self.solve(arr, n, ls, i + 1, s)
                s = s.removesuffix(arr[i])
                self.solve(arr, n, ls, i + 1, s)

        return ls

    def isUnique(self, s):
        return len(s) == len(set(s))
