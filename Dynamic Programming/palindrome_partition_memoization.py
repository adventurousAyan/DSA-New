class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        return self.solve(0, n, s, float("inf"), dp) - 1

    def solve(self, i, n, s, mincost, dp):
        if i == n:
            return 0
        if dp[i] != -1:
            return dp[i]
        else:
            temp = ""
            for j in range(i, n):
                temp += s[j]
                if self.isPalindrome(temp):
                    cost = 1 + self.solve(j + 1, n, s, mincost, dp)
                    mincost = min(mincost, cost)
            dp[i] = mincost
            return dp[i]

    def isPalindrome(self, s):
        lp = 0
        rp = len(s) - 1
        s = list(s)
        while lp <= rp:
            if s[lp] != s[rp]:
                return False
            lp += 1
            rp -= 1
        return True
