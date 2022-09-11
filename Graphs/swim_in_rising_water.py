import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        # Check for validity
        def is_valid(nr, nc):
            return nr >= 0 and nr < m and nc >= 0 and nc < n and visited[nr][nc] != 1

        m, n = len(grid), len(grid[0])
        # Declare a priority queue
        minq = []
        # Declare visited array
        visited = [[-1] * n for _ in range(m)]

        # Initially push grid val, row, col, and time into queue
        heapq.heappush(minq, (grid[0][0], 0, 0, 0))

        while len(minq) > 0:
            val, r, c, time = heapq.heappop(minq)
            # If the current time is less than grid val(elevation), increase time and submit to queue
            if time < val:
                heapq.heappush(minq, (grid[r][c], r, c, time + 1))
                continue

            # Base Case
            if r == m - 1 and c == n - 1:
                return time
            # Mark the cell visited
            visited[r][c] = 1
            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

            for nr, nc in directions:
                if is_valid(nr, nc):
                    # It means that the elevation is less than the timestamp. Hnece no need to increase time
                    if grid[nr][nc] < time:
                        heapq.heappush(minq, (grid[nr][nc], nr, nc, time))
                    else:
                        # Here elevation is greater than time. Hence we need to increase the timestamp
                        heapq.heappush(minq, (grid[nr][nc], nr, nc, time + 1))

        return -1
