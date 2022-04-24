class Solution:
    # https://practice.geeksforgeeks.org/problems/gold-mine-problem2608/1#

    def maxGold(self, n, m, M):
        # code here
        maxno = float("-inf")
        dp = [[-1] * (m) for i in range(n)]
        for i in range(n):
            res = self.solve(i, 0, n, m, M, float("-inf"), dp)
            maxno = max(res, maxno)
        return maxno

    def solve(self, row, col, n, m, nums, maxno, dp):

        if not (row >= 0 and row <= n - 1 and col >= 0 and col <= m - 1):
            return 0
        if dp[row][col] != -1:
            return dp[row][col]
        else:
            diagup = nums[row][col] + self.solve(
                row - 1, col + 1, n, m, nums, maxno, dp
            )
            right = nums[row][col] + self.solve(row, col + 1, n, m, nums, maxno, dp)
            digdown = nums[row][col] + self.solve(
                row + 1, col + 1, n, m, nums, maxno, dp
            )
            maxno = max(maxno, diagup, right, digdown)
            dp[row][col] = maxno
        return dp[row][col]
