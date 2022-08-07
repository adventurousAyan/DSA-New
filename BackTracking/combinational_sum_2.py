from typing import List


class Solution:
    # https://leetcode.com/problems/combination-sum-ii/

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(target, arr, i, l1):
            if target == 0:
                l1 = l1.copy()
                self.ls.append(l1)
                return
            if i > len(arr) - 1:
                return
            if target >= arr[i]:
                l1.append(arr[i])
                solve(target - arr[i], arr, i + 1, l1)
                l1.pop()

            while i + 1 < len(arr) and arr[i] == arr[i + 1]:
                i += 1
            solve(target, arr, i + 1, l1)

        arr = sorted(candidates)
        self.ls = []
        solve(target, arr, 0, [])
        return self.ls
