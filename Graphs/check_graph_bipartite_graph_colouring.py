from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/is-graph-bipartite/


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)

        d1 = defaultdict(list)
        color = [-1] * n

        for i in range(len(graph)):
            d1[i].extend(graph[i])

        def bfs(node):
            q = deque()
            q.append((node, 1))
            color[node] = 1

            while len(q) > 0:

                item, cur_color = q.popleft()
                neighbrs = d1[item]
                for nei in neighbrs:
                    if color[nei] == -1:
                        color[nei] = 1 - cur_color
                        q.append((nei, 1 - cur_color))
                    elif color[nei] == cur_color:
                        return False

            return True

        for i in range(n):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True
