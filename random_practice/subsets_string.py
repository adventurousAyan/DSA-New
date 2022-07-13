from typing import List

# https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ls = []

        def solve(nums, j, s):

            if j == n:
                ls.append(s.copy())
            else:
                # Exclude
                solve(nums, j + 1, s)
                # Include
                s.append(nums[j])
                solve(nums, j + 1, s)
                s.pop()

        solve(nums, 0, [])
        return ls
