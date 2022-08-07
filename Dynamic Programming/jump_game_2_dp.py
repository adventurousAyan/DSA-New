from typing import List

# https://leetcode.com/problems/jump-game-ii/


class Solution:
    def jump(self, nums: List[int]) -> int:

        mini = float("inf")
        n = len(nums)
        dp = [0] * n
        return self.f(0, n, nums, mini, dp)

    def f(self, idx, n, nums, mini, dp):

        if idx >= n:
            return float("inf")

        elif dp[idx] != 0:
            return dp[idx]

        elif idx == n - 1:
            return 0

        for i in range(1, nums[idx] + 1):
            mini = min(mini, 1 + self.f(idx + i, n, nums, mini, dp))

        dp[idx] = mini

        return dp[idx]
