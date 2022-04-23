from typing import List

# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        for i in range(n):
            if i == 0 or i == 1:
                dp[i] = max(nums[i], dp[i - 1])
            else:
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[n - 1]
