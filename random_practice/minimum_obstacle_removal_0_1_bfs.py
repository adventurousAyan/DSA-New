from collections import deque
from typing import List

# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        def is_valid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n and visited[i][j] != 1

        def bfs():
            q.append((0, 0, 0))
            visited[0][0] = 1
            mini = float("inf")
            while len(q) != 0:

                move, i, j = q.popleft()

                if i == m - 1 and j == n - 1:
                    # If we reach the end, check the minimum and reset the visited as this can be visited
                    # by any other path
                    mini = min(mini, move)
                    visited[m - 1][n - 1] = -1
                    continue

                # up
                if is_valid(i - 1, j):
                    visited[i - 1][j] = 1
                    val1 = grid[i - 1][j]
                    if val1 == 1:
                        q.append((move + 1, i - 1, j))
                    else:
                        q.appendleft((move, i - 1, j))

                # right
                if is_valid(i, j + 1):
                    visited[i][j + 1] = 1
                    val1 = grid[i][j + 1]
                    if val1 == 1:
                        q.append((move + 1, i, j + 1))
                    else:
                        q.appendleft((move, i, j + 1))

                # down
                if is_valid(i + 1, j):
                    visited[i + 1][j] = 1
                    val1 = grid[i + 1][j]
                    if val1 == 1:
                        q.append((move + 1, i + 1, j))
                    else:
                        q.appendleft((move, i + 1, j))

                # left
                if is_valid(i, j - 1):
                    visited[i][j - 1] = 1
                    val1 = grid[i][j - 1]
                    if val1 == 1:
                        q.append((move + 1, i, j - 1))
                    else:
                        q.appendleft((move, i, j - 1))

            return mini

        m = len(grid)
        n = len(grid[0])

        q = deque()

        visited = [[-1] * n for _ in range(m)]
        return bfs()
