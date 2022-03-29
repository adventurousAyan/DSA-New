class Solution:
    def matrixMultiplication(self, N, arr):
        # code here

        i = 1
        j = N - 1
        dp = [[None] * 501 for i in range(501)]
        return self.solve(i, j, arr, dp)

    def solve(self, i, j, arr, dp):
        minno = float("inf")
        if dp[i][j] is not None:
            return dp[i][j]
        elif i >= j:
            dp[i][j] = 0
            return 0
        else:
            for k in range(i, j):
                temp = (
                    self.solve(i, k, arr, dp)
                    + self.solve(k + 1, j, arr, dp)
                    + arr[i - 1] * arr[k] * arr[j]
                )
                if temp < minno:
                    minno = temp
            dp[i][j] = minno
            return minno
