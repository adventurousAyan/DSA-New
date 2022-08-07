from collections import defaultdict
from typing import List

# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
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

        for stone in stones:
            row = stone[0]
            col = stone[1] + 10001
            parent[row] = row
            parent[col] = col
        self.count = len(parent)

        for stone in stones:
            row = stone[0]
            col = stone[1] + 10001
            union(row, col)

        connect_components = self.count
        # No of stones to be removed = No of stones - connect_components
        # No of connected components is no of root
        return len(stones) - connect_components
