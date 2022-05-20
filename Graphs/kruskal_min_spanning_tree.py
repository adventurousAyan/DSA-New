# User function Template for python3

# https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1#


class Solution:

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        # code here
        self.parent = [-1] * V
        self.rank = [0] * V
        self.make_set(V)
        min_mst = 0
        ls = []
        for i in range(V):
            for val in adj[i]:
                ls.append((i, val[0], val[1]))
        ls = sorted(ls, key=lambda x: x[2])
        for val in ls:
            if self.find_par(val[0]) != self.find_par(val[1]):
                min_mst += val[2]
                self.union(val[0], val[1])
        return min_mst

    def make_set(self, v):
        for i in range(v):
            self.parent[i] = i
            self.rank[i] = 0

    def find_par(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_par(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        u = self.find_par(u)
        v = self.find_par(v)
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        elif self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[v] = u
            self.rank[u] += 1
