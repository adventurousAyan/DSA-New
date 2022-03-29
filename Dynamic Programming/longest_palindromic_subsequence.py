class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        str1 = s
        str2 = s[::-1]
        n = len(s)

        dp = [[None] * (n + 1) for i in range(n + 1)]

        for i in range(n + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    if str1[i - 1] == str2[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][n]
