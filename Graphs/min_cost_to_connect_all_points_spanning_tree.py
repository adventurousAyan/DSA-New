from collections import defaultdict
from typing import List

# https://leetcode.com/problems/min-cost-to-connect-all-points/


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find_par(node):
            if parent[node] != node:
                parent[node] = find_par(parent[node])
            return parent[node]

        def union(u, v):
            u = find_par(u)
            v = find_par(v)
            if u == v:
                return
            self.count -= 1

            if rank[u] < rank[v]:
                parent[u] = v
            elif rank[u] > rank[v]:
                parent[v] = u
            else:
                parent[v] = u
                rank[u] += 1

        rank = defaultdict(int)
        parent = {}
        self.count = 0
        min_cost = 0

        n = len(points)
        ls = []
        # Convert all 2D points into 1D points using row*total_col_length + col
        # Pair all points and take absolute of manhattan distance
        # Now the problem reduces to finding the minimum spanning tree
        for i in range(n):
            for j in range(i + 1, n):
                xi = points[i][0]
                xj = points[j][0]
                yi = points[i][1]
                yj = points[j][1]
                point1 = xi * 1000001 + yi
                point2 = xj * 1000001 + yj
                ls.append((point1, point2, abs(xi - xj) + abs(yi - yj)))
                parent[point1] = point1
                parent[point2] = point2

        self.count = len(parent)
        ls = sorted(ls, key=lambda x: x[2])
        for val in ls:
            if find_par(val[0]) != find_par(val[1]):
                union(val[0], val[1])
                min_cost += val[2]
        return min_cost
