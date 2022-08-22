from typing import Deque, List

# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        # Is Valid check
        def is_valid(r, c, obs):
            return r >= 0 and r < m and c >= 0 and c < n and (r, c, obs) not in visited

        m = len(grid)
        n = len(grid[0])
        q = Deque()
        q.append((0, 0, 0, 0))
        obs = 0
        # Maintain a 3d grid of pathLen, rowNo, colNo and obstacles
        visited = set()
        while len(q) > 0:
            pathLen, r, c, obs = q.popleft()

            # Base Case
            if r == m - 1 and c == n - 1:
                return pathLen

            # If obstacle count is more than k , then return
            if obs > k and grid[r][c] == 1:
                continue

            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

            for nr, nc in directions:
                # 1 means, its a obstacle, so increase the obstacle count
                if is_valid(nr, nc, obs + 1) and grid[nr][nc] == 1:
                    q.append((pathLen + 1, nr, nc, obs + 1))
                    visited.add((nr, nc, obs + 1))
                # 0 means no obstacle, so obstacle count remains same
                if is_valid(nr, nc, obs) and grid[nr][nc] == 0:
                    q.append((pathLen + 1, nr, nc, obs))
                    visited.add((nr, nc, obs))
        return -1
