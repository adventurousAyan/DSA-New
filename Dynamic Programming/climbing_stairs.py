class Solution:
    def climbStairs(self, n: int) -> int:
        ls = [-1] * (n + 1)
        ls[n] = 1
        ls[n - 1] = 1

        for i in range(n - 2, -1, -1):
            ls[i] = ls[i + 1] + ls[i + 2]
        return ls[0]
