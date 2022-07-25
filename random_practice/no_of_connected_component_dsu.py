from typing import List

# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find_par(node):
            if parent[node] == -1:
                return node
            parent[node] = find_par(parent[node])
            return parent[node]

        def union(u, v):
            u = find_par(u)
            v = find_par(v)

            if rank[u] < rank[v]:
                parent[u] = v
            elif rank[u] > rank[v]:
                parent[v] = u
            else:
                parent[v] = u
                rank[u] += 1

        parent = [-1] * n
        rank = [0] * n

        for edge in edges:
            if find_par(edge[0]) != find_par(edge[1]):
                union(edge[0], edge[1])

        connect_components = 0
        # No of connected components is no of root
        for val in parent:
            if val == -1:
                connect_components += 1
        return connect_components
