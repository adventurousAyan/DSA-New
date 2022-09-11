from typing import List

# https://leetcode.com/problems/making-a-large-island/


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        # Check for is_valid
        def is_valid(nr, nc):
            return (
                nr >= 0
                and nr < m
                and nc >= 0
                and nc < n
                and grid[nr][nc] == 1
                and visited[nr][nc] != 1
            )

        # DFS to find the area of the island
        def dfs(r, c):
            visited[r][c] = 1
            # Mark the island with the island_id
            grid[r][c] = self.island_id

            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

            res = 0

            for nr, nc in directions:
                if is_valid(nr, nc):
                    res += 1 + dfs(nr, nc)
            return res

        # Calculate the area
        def calculate_area(r, c):

            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

            area = 0
            myset = set()
            # Here we take the neighboring island id's and put it to a set as
            # it may contain same id
            for nr, nc in directions:
                if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] != 0:
                    myset.add(grid[nr][nc])
            # Loop through the set and add the area
            for val in myset:
                area += iland_map[val]
            # Return area + 1 for the current cell 0 which we can change to 1 to make large island
            return area + 1

        m, n = len(grid), len(grid[0])

        # Declarations
        visited = [[-1] * n for _ in range(m)]
        self.island_id = 2
        iland_map = {}
        max_area = 1
        # Loop through row and col and do dfs for calculating area. Store the area of
        # a particular island in map using key as island_id and value as the area
        # Increment the island id for the next iteration
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and visited[r][c] != 1:
                    res = 1 + dfs(r, c)
                    max_area = max(max_area, res)
                    iland_map[self.island_id] = res
                    self.island_id += 1

        # Now we need to calculate the max area by changing atmost one 0 to 1
        # We assign a maxi variable which is equal to the max area obtained in above step
        # By changing one 0 to 1, we will see if this maxi changes to a large value and
        # we have to return the area of the large island
        maxi = max_area
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res = calculate_area(i, j)
                    maxi = max(maxi, res)
        return maxi
