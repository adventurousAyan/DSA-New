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

        m, n = len(word1), len(word2)
        dp = [[-1] * (501) for _ in range(501)]
        f(m, n)
        return dp[m][n]
