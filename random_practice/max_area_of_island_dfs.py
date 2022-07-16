from typing import List

# https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def is_safe(i, j, m, n):
            return (
                i >= 0
                and i < m
                and j >= 0
                and j < n
                and grid[i][j] == 1
                and visited[i][j] == -1
            )

        def dfs(i, j, m, n):
            if grid[i][j] == 1 and visited[i][j] == -1:
                visited[i][j] = 1

            # Up
            u, d, l, r = 0, 0, 0, 0
            if is_safe(i - 1, j, m, n):
                u = 1 + dfs(i - 1, j, m, n)

            # Down
            if is_safe(i + 1, j, m, n):
                d = 1 + dfs(i + 1, j, m, n)

            # Left
            if is_safe(i, j - 1, m, n):
                l = 1 + dfs(i, j - 1, m, n)

            # Right
            if is_safe(i, j + 1, m, n):
                r = 1 + dfs(i, j + 1, m, n)

            return u + d + l + r

        maxi = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == -1:
                    maxi = max(1 + dfs(i, j, m, n), maxi)
        return maxi
