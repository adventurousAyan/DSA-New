class Solution:
    # https://leetcode.com/problems/maximal-square/

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def f(r, c):
            # Base Case
            if not (r >= 0 and r < m and c >= 0 and c < n):
                return 0
            if matrix[r][c] == "0":
                return 0
            if dp[r][c] != -1:
                return dp[r][c]

            right = f(r, c + 1)
            down = f(r + 1, c)
            diagdown = f(r + 1, c + 1)

            dp[r][c] = 1 + min(right, down, diagdown)
            return dp[r][c]

        m, n = len(matrix), len(matrix[0])
        maxi = 0
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                maxi = max(maxi, f(i, j))
                dp[i][j] = maxi

        res = dp[m - 1][n - 1]
        return res * res


####################2nd Approach#################################################


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def f(r, c):
            # Base Case
            if not (r >= 0 and r < m and c >= 0 and c < n):
                return 0
            if dp[r][c] != -1:
                return dp[r][c]

            right = f(r, c + 1)
            down = f(r + 1, c)
            diagdown = f(r + 1, c + 1)

            if matrix[r][c] == "1":
                dp[r][c] = 1 + min(right, down, diagdown)
                self.maxi = max(self.maxi, dp[r][c])
                return dp[r][c]
            else:
                dp[r][c] = 0
                return dp[r][c]

        m, n = len(matrix), len(matrix[0])
        self.maxi = 0
        dp = [[-1] * (n) for _ in range(m)]
        f(0, 0)
        return self.maxi * self.maxi
