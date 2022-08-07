from collections import defaultdict
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        visited = [[-1] * n for _ in range(m)]
        num_islands = 0

        def is_valid(i, j):
            return (
                i >= 0
                and i < m
                and j >= 0
                and j < n
                and grid[i][j] == 0
                and visited[i][j] != 1
            )

        def dfs(i, j):

            if grid[i][j] == 0 and visited[i][j] == -1:
                visited[i][j] = 1

            directions = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]

            for dir in directions:
                row, col = dir[0], dir[1]

                if is_valid(row, col):
                    dfs(row, col)

        for i in range(m):
            for j in [0, n - 1]:
                if grid[i][j] == 0 and visited[i][j] != 1:
                    dfs(i, j)

        for i in [0, m - 1]:
            for j in range(n):
                if grid[i][j] == 0 and visited[i][j] != 1:
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and visited[i][j] != 1:
                    num_islands += 1
                    dfs(i, j)
        return num_islands
