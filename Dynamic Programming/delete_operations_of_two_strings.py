class Solution:

    # https://leetcode.com/problems/delete-operation-for-two-strings/
    # This problem is mostly similar to Edit Distance. See top down for
    # edit distance solution as well

    def minDistance(self, word1: str, word2: str) -> int:
        def f(i, j):
            # Base Case
            if dp[i][j] != -1:
                return dp[i][j]
            if j == 0:
                dp[i][0] = i
                return i
            if i == 0:
                dp[0][j] = j
                return j

            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = f(i - 1, j - 1)
            else:
                dp[i][j] = 1 + min(f(i - 1, j), f(i, j - 1))
            return dp[i][j]

        def f_td():
            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0:
                        dp[i][j] = j
                    elif j == 0:
                        dp[i][j] = i
                    else:
                        if word1[i - 1] == word2[j - 1]:
                            dp[i][j] = dp[i - 1][j - 1]
                        else:
                            dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j])

        m, n = len(word1), len(word2)
        dp = [[-1] * (501) for _ in range(501)]
        f(m, n)
        # f_td()
        return dp[m][n]
