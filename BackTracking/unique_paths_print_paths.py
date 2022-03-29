class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        i = 0
        j = 0
        self.val = 0
        s = ""
        ls = []
        self.solve(i, j, m, n, s, ls)
        print(ls)
        return self.val

    def solve(self, i, j, m, n, s, ls):
        if i == m - 1 and j == n - 1:
            self.val = self.val + 1
            ls.append(s)
        else:
            if i <= m - 1:
                self.solve(i + 1, j, m, n, s + "D", ls)
            if j <= n - 1:
                self.solve(i, j + 1, m, n, s + "R", ls)
