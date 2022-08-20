"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        def dfs(root):
            if root is None:
                return root

            dfs(root.left)
            if self.last:
                self.last.right = root
                root.left = self.last
            else:
                self.first = root
            self.last = root
            dfs(root.right)

        self.last = None
        self.first = None
        dfs(root)
        if self.last:
            self.last.right = self.first
        if self.first:
            self.first.left = self.last
        return self.first
