from typing import List

# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:

        grid = [[float("inf")] * n for i in range(n)]
        d1 = {}
        minno = float("inf")
        maxno = float("-inf")
        for val in edges:
            grid[val[0]][val[1]] = val[2]
            grid[val[1]][val[0]] = val[2]

        res = self.floydWarshal(grid, n)

        for i in range(n):
            ln = len([x for x in res[i] if x != 0 and x <= distanceThreshold])
            minno = min(minno, ln)
            d1[i] = d1.get(i, 0) + ln

        for k, v in d1.items():
            if d1[k] == minno:
                maxno = max(k, maxno)
        return maxno

    def floydWarshal(self, grid, n):

        dv = grid

        for i in range(n):
            for j in range(n):
                if i == j:
                    dv[i][j] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dv[i][k] == float("inf") or dv[k][j] == float("inf"):
                        continue
                    if dv[i][k] + dv[k][j] < dv[i][j]:
                        dv[i][j] = dv[i][k] + dv[k][j]
        return dv
