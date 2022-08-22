from typing import List

# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # Is Valid check where the new row and col values should be more than
        # the existing values
        def is_valid(nr, nc, r, c):
            return (
                nr >= 0
                and nr < m
                and nc >= 0
                and nc < n
                and matrix[nr][nc] > matrix[r][c]
            )

        def dfs(r, c, dp):

            # Memoization
            if dp[r][c] != -1:
                return dp[r][c]

            directions = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]

            # Initialise maxi to 1 as pathLen will always be one
            # i.e a single cell
            maxi = 1
            for diri in directions:
                if is_valid(diri[0], diri[1], r, c):
                    # This will fetch the longest path and add 1 for the current cell
                    res = 1 + dfs(diri[0], diri[1], dp)
                    maxi = max(maxi, res)

            dp[r][c] = maxi
            return dp[r][c]

        m = len(matrix)
        n = len(matrix[0])

        # Declare a DP array
        dp = [[-1] * n for _ in range(m)]

        # We need to loop through all the cells in order to
        # find the longest incresing
        maxi = float("-inf")
        for r in range(m):
            for c in range(n):
                res = dfs(r, c, dp)
                maxi = max(maxi, res)

        return maxi
