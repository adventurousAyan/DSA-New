class Solution:

    # https://leetcode.com/problems/decode-ways/

    def numDecodings(self, s: str) -> int:

        n = len(s)

        def f(i):

            if dp[i] != -1:
                return dp[i]
            pick1, pick2 = 0, 0
            if s[i] != "0":
                pick1 = f(i + 1)
            else:
                dp[i] = 0
                return dp[i]
            if i + 1 < n and int(s[i : i + 2]) <= 26:
                pick2 = f(i + 2)
            dp[i] = pick1 + pick2
            return dp[i]

        dp = [-1] * (n + 1)
        dp[n] = 1
        f(0)
        return dp[0]
