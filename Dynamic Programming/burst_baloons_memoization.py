class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        n = len(nums)
        nums = [1] + nums + [1]

        def f(i, j):

            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            maxi = 0
            for k in range(i, j + 1):
                coins = nums[i - 1] * nums[k] * nums[j + 1] + f(i, k - 1) + f(k + 1, j)
                maxi = max(maxi, coins)
            dp[i][j] = maxi
            return maxi

        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        return f(1, n)
