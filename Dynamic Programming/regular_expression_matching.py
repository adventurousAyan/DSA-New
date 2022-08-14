class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def f(i, j):
            # Base Case:
            # Both are strings have been exhausted
            if i < 0 and j < 0:
                return True
            if i < 0 and p[j] == "*":
                # The string has exhausted but the pattern has a * and it can match zero or more
                # characters
                return f(i, j - 2)
            if i < 0 and p[j] == ".":
                # The string has exhausted but pattern contains a "."
                return False
            if i < 0 or j < 0:
                # The pattern has exhausted
                return False

            if dp[i][j] != -1:
                # Memoization
                return dp[i][j]
            else:
                if s[i] == p[j]:
                    # Matches move forward
                    dp[i][j] = f(i - 1, j - 1)
                    return dp[i][j]
                else:
                    if p[j] == ".":
                        # . matches any single character. So move forward
                        dp[i][j] = f(i - 1, j - 1)
                        return dp[i][j]
                    elif p[j] == "*":
                        # * match zero or more of its preceeding character. So when there is a match,
                        #   move forward
                        if p[j - 1] == s[i] or p[j - 1] == ".":
                            dp[i][j] = f(i - 1, j) or f(i, j - 2)
                            return dp[i][j]
                        else:
                            # If not match, move to the previous character in pattern
                            dp[i][j] = f(i, j - 2)
                            return dp[i][j]
                    else:
                        # Rest in all cases return false
                        dp[i][j] = False
                        return dp[i][j]

        m, n = len(s), len(p)
        dp = [[-1] * (n) for _ in range(m)]
        f(m - 1, n - 1)
        return dp[m - 1][n - 1]
