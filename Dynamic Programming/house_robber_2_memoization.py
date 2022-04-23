from typing import List

# https://leetcode.com/problems/house-robber-ii/submissions/


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [-1] * n
        res1 = self.solve(n - 2, nums[1:], dp)
        dp = [-1] * n
        res2 = self.solve(n - 2, nums[: n - 1], dp)
        return max(res1, res2)

    def solve(self, n, nums, dp):
        if dp[n] != -1:
            return dp[n]
        if n < 0:
            return 0
        elif n == 0:
            dp[n] = nums[n]
        else:
            tmp1 = nums[n] + self.solve(n - 2, nums, dp)
            tmp2 = self.solve(n - 1, nums, dp)
            dp[n] = max(tmp1, tmp2)
        return dp[n]
