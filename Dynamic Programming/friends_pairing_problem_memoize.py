class Solution:
    # https://practice.geeksforgeeks.org/problems/friends-pairing-problem5425/1#
    def countFriendsPairings(self, n):
        # code here
        dp = [-1] * (n + 1)
        return self.solve(n, 0, pow(10, 9) + 7, dp)

    def solve(self, n, ss, mod, dp):
        if n == 0 or n == 1:
            dp[n] = 1
            return dp[n]
        elif dp[n] != -1:
            return dp[n]
        else:
            single = self.solve(n - 1, ss, mod, dp) % mod
            pair = ((n - 1) * self.solve(n - 2, ss, mod, dp)) % mod
            ss = (single + pair) % mod
            dp[n] = ss
        return dp[n]
