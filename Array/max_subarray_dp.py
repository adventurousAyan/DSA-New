from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        s = 0
        maxsum = float("-inf")
        return self.solve(n, nums, s, maxsum)

    def solve(self, n, nums, s, maxsum, memo={}):
        if memo.get(n) is not None:
            return memo[n]
        if n == 0:
            return maxsum
        else:
            for i in range(n - 1, -1, -1):
                s = s + nums[i]
                if s < 0:
                    s = 0
                if s > maxsum:
                    maxsum = s
                memo[n - 1] = self.solve(n - 1, nums, s, maxsum, memo)
                return memo[n - 1]


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
