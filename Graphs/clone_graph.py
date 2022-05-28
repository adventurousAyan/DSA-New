"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# https://leetcode.com/problems/clone-graph/


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":

        d1 = {}

        def dfs(node):
            if d1.get(node, None):
                return d1[node]
            else:
                copy = Node(node.val)
                d1[node] = copy
                for nei in node.neighbors:
                    copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node is not None else None
