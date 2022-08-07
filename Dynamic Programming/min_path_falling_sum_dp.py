from typing import List

# https://leetcode.com/problems/minimum-falling-path-sum/


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def f(i, j, dp):
            # Base Case:
            # If boundary condition exceeds, return a larger value so that it wont be taken into consideration
            if not (i >= 0 and i < m and j >= 0 and j < n):
                return float("inf")
            # Memoize
            if dp[i][j] != -1:
                return dp[i][j]
            if i == 0:
                dp[i][j] = matrix[i][j]
                return dp[i][j]

            # Calculate the rising path sum as it is top down
            dp[i][j] = matrix[i][j] + min(
                f(i - 1, j - 1, dp), f(i - 1, j, dp), f(i - 1, j + 1, dp)
            )
            return dp[i][j]

        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        # Loop through the last row to calculate the falling sum for each element in last row
        for i in range(n):
            dp[m - 1][i] = f(m - 1, i, dp)

        return min(dp[m - 1])
