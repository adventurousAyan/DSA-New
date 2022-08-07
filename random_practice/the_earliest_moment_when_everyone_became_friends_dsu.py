from collections import defaultdict
from typing import List

# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
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
        logs = sorted(logs, key=lambda x: x[0])

        for i in range(n):
            parent[i] = i
        self.count = len(parent)

        for log in logs:
            union(log[1], log[2])
            if self.count == 1:
                return log[0]
        return -1
