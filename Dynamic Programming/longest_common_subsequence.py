# User function Template for python3


class Solution:

    # Function to find the length of longest common subsequence in two strings.
    def lcs(self, x, y, s1, s2):

        # code here
        dp = [[None] * (y + 1) for i in range(x + 1)]

        for i in range(x + 1):
            for j in range(y + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # print(dp)
        return dp[x][y]
