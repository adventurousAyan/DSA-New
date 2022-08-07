from collections import defaultdict, deque
from typing import List

# This is based on Kahns alo for topo sort using BFS. understand kahns algi, inorder
# to understand it fully


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        d1 = defaultdict(list)

        degree = [0] * n

        for edge in edges:
            d1[edge[0]].append(edge[1])
            d1[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1

        q = deque()

        for i in range(n):
            if degree[i] == 1:
                q.append(i)
                degree[i] -= 1
        ls = []
        while q:
            ls = []
            for _ in range(len(q)):
                node = q.popleft()
                ls.append(node)
                for nei in d1[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        return ls if ls else [0]
