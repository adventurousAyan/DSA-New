class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def f(i, j):
            # Base Case:

            if i < 0 and j < 0:
                return True
            if i < 0 and p[j] == "*":
                return f(i, j - 2)
            if i < 0 and p[j] == ".":
                return False
            if i < 0 or j < 0:
                return False

            if dp[i][j] != -1:
                return dp[i][j]
            else:
                if s[i] == p[j]:
                    dp[i][j] = f(i - 1, j - 1)
                    return dp[i][j]
                else:
                    if p[j] == ".":
                        dp[i][j] = f(i - 1, j - 1)
                        return dp[i][j]
                    elif p[j] == "*":
                        if p[j - 1] == s[i] or p[j - 1] == ".":
                            dp[i][j] = f(i - 1, j) or f(i, j - 2)
                            return dp[i][j]
                        else:
                            dp[i][j] = f(i, j - 2)
                            return dp[i][j]
                    else:
                        dp[i][j] = False
                        return dp[i][j]

        m, n = len(s), len(p)
        dp = [[-1] * (n) for _ in range(m)]
        f(m - 1, n - 1)
        return dp[m - 1][n - 1]
