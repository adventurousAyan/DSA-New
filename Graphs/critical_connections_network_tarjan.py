from collections import defaultdict
from typing import List

# https://leetcode.com/problems/critical-connections-in-a-network/

# https://www.youtube.com/watch?v=2rjZH0-2lhk
# https://www.youtube.com/watch?v=RYaakWv5m6o
# https://www.youtube.com/watch?v=CiDPT1xMKI0


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:

        adj = defaultdict(list)

        for conn in connections:
            u, v = conn[0], conn[1]
            adj[u].append(v)
            adj[v].append(u)

        # print(adj)
        def dfs(node, par):

            visited[node] = True

            lowest[node] = self.next_id
            disc[node] = self.next_id
            self.next_id += 1
            for nei in adj[node]:
                if nei == par:
                    continue
                if not visited[nei]:
                    dfs(nei, node)
                    lowest[node] = min(lowest[node], lowest[nei])
                    # Check for bridge
                    if lowest[nei] > disc[node]:
                        ls.append([node, nei])
                else:
                    # Node already visited and not parent
                    # Back- edge
                    lowest[node] = min(lowest[node], disc[nei])

        ls = []
        self.next_id = 0
        lowest = [-1] * n
        disc = [-1] * n
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                dfs(i, -1)
        return ls
