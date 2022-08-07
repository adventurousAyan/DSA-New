from queue import Queue
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Check validity of a fresh orange
        def is_valid(i, j):
            return (
                i >= 0
                and i < m
                and j >= 0
                and j < n
                and grid[i][j] == 1
                and visited[i][j] != 1
            )

        # Check validity  if there is any fresh orange
        def is_valid_dfs(i, j):
            return (
                i >= 0
                and i < m
                and j >= 0
                and j < n
                and grid[i][j] != 2
                and visited[i][j] != 1
            )

        def bfs():
            maxi = 0
            q = Queue()
            for i in range(m):
                for j in range(n):
                    # Put all rotten oranges first in queue
                    if grid[i][j] == 2 and visited[i][j] != 1:
                        q.put((i, j, 0))

            # Now pop rotten elements and visit nearby elements
            while not q.empty():
                i, j, time = q.get()
                # This check is necessary as the cell might have already visited with a lower time
                if visited[i][j] == -1:
                    grid[i][j] = 2
                    visited[i][j] = 1
                    maxi = time
                # Up
                if is_valid(i - 1, j):
                    q.put((i - 1, j, time + 1))
                # Down
                if is_valid(i + 1, j):
                    q.put((i + 1, j, time + 1))
                # Left
                if is_valid(i, j - 1):
                    q.put((i, j - 1, time + 1))
                # Right
                if is_valid(i, j + 1):
                    q.put((i, j + 1, time + 1))
            return maxi

        def dfs(i, j, visited):
            visited[i][j] = 1
            # That means we still have a fresh orange.
            if grid[i][j] == 1:
                return False
            # Up
            up, down, left, right = True, True, True, True
            if is_valid_dfs(i - 1, j):
                up = dfs(i - 1, j, visited)
            # Down
            if is_valid_dfs(i + 1, j):
                down = dfs(i + 1, j, visited)
            # Left
            if is_valid_dfs(i, j - 1):
                left = dfs(i, j - 1, visited)
            # Right
            if is_valid_dfs(i, j + 1):
                right = dfs(i, j + 1, visited)
            return up and down and left and right

        m = len(grid)
        n = len(grid[0])
        visited = [[-1] * n for _ in range(m)]
        maxi = bfs()

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 2 and visited[i][j] != 1:
                    # Do dfs traversal to check for any fresh orange. If there is one, just return -1
                    res = dfs(i, j, visited)
                    if not res:
                        return -1

        # It means there is no fresh orange left, hence return the minimum time
        return maxi
