from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        self.visited = [["-1"] * (n) for i in range(m)]

        noofislands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and self.visited[i][j] == "-1":
                    noofislands += 1
                    self.dfs(grid, i, j, m, n)
        # print(self.visited)
        return noofislands

    def dfs(self, grid, i, j, m, n):

        if grid[i][j] == "1" and self.visited[i][j] == "-1":
            self.visited[i][j] = "1"

        # Left
        if self.isSafe(grid, i - 1, j, m, n):
            self.dfs(grid, i - 1, j, m, n)

        # Right
        if self.isSafe(grid, i + 1, j, m, n):
            self.dfs(grid, i + 1, j, m, n)

        # Top
        if self.isSafe(grid, i, j - 1, m, n):
            self.dfs(grid, i, j - 1, m, n)

        # Down
        if self.isSafe(grid, i, j + 1, m, n):
            self.dfs(grid, i, j + 1, m, n)

    def isSafe(self, grid, i, j, m, n):

        if (
            i >= 0
            and i < m
            and j >= 0
            and j < n
            and grid[i][j] == "1"
            and self.visited[i][j] != "1"
        ):
            return True
        else:
            return False
