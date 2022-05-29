# https://practice.geeksforgeeks.org/problems/alien-dictionary/1#


class Solution:
    def findOrder(self, dict, N, K):
        # code here
        # Convert to list
        words = list(dict)
        # Initialize the adjacency list
        d1 = {c: set() for w in words for c in w}

        # Construct the adjacency list
        n = len(words)
        for i in range(n - 1):
            w1 = words[i]
            w2 = words[i + 1]
            m = 0
            n = 0
            while m < len(w1) and n < len(w2):
                if w1[m] != w2[n]:
                    d1[w1[m]]
                    d1[w1[m]].add(w2[n])
                    break
                else:
                    m += 1
                    n += 1

        # Do Topological Sort
        nodes = list(d1.keys())
        visited = {}
        for node in nodes:
            visited[node] = 0
        ls = []

        def dfs(node):
            if visited[node] == 1:
                return
            visited[node] = 1
            neighbors = d1[node]
            for nei in neighbors:
                dfs(nei)
            ls.append(node)

        for node in nodes:
            if visited[node] == 0:
                dfs(node)

        # Reverse and return the answer
        return ls[::-1]
