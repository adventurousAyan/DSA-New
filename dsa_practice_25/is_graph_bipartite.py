class Solution:
    from collections import deque
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        
        def dfs(node):
            vis1[node] = 1
            for nei in graph[node]:
                if vis1[nei] == -1:
                    dfs(nei)
        
        def find_connected_com():
            for i in range(n):
                if vis1[i] == -1:
                    dfs(i)
                    ls.append(i)
            return ls


        
        n = len(graph)
        ls = []

        queue = deque()
        
   
        vis = [-1]*n
        vis1 = [-1]*n
        color = [-1]*n

        ls = find_connected_com()

        col = 0
        
        for item in ls:
            queue.append((item, col))

        while len(queue) > 0:
            node, col = queue.popleft()
            vis[node] = 1
            color[node] = col
            col ^=1
            for nei in graph[node]:
                if vis[nei] == -1:
                    queue.append((nei, col))
        d = {}
        for idx, val in enumerate(color):
            if not d.get(val):
                d[val] = [idx]
            else:
                d[val].append(idx)
        for idx, items in enumerate(graph):
            for item in items:
                res = ((idx in d[0] and item in d[1]) or (item in d[0] and idx in d[1]))
                if not res:
                    return False
        return True



# https://leetcode.com/problems/is-graph-bipartite/


# Optimal Approach - BFS
# Eliminate DFS to find connected components as the same can be done with BFS as well
# No need to loop and again check for colors sincewe can acheck adjacent nodes color and if it is same then return False

class Solution:
    from collections import deque
    def isBipartite(self, graph: List[List[int]]) -> bool:
    
        n = len(graph)
        queue = deque()
        
   
        vis = [-1]*n
        color = [-1]*n
        col = 0
        
        for i in range(n):
            if vis[i] == -1:
                queue.append((i, col))

            while len(queue) > 0:
                node, col = queue.popleft()
                vis[node] = 1
                color[node] = col
                col ^=1
                for nei in graph[node]:
                    if vis[nei] == -1:
                        queue.append((nei, col))
                    elif color[nei] == color[node]:
                        return False
        return True
        
                

        



      






        
                

        



      






        