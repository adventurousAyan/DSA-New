class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        i = 0
        j = 0
        self.val = 0
        self.solve(i, j, m, n)
        return self.val

    def solve(self, i, j, m, n):
        if i == m - 1 and j == n - 1:
            self.val = self.val + 1
        else:
            if i <= m - 1:
                self.solve(i + 1, j, m, n)
            if j <= n - 1:
                self.solve(i, j + 1, m, n)
