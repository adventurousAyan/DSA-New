from typing import List

# https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        i, j = 0, 0
        n = len(nums)
        su = 0
        mini = float("inf")
        arr = nums

        if sum(arr) < target:
            return 0

        while j < n:

            su += arr[j]

            if su < target:
                j += 1
            elif su == target:
                mini = min(mini, j - i + 1)
                j += 1
            else:
                while su >= target:
                    mini = min(mini, j - i + 1)
                    su -= arr[i]
                    i += 1
                j += 1

        return mini
