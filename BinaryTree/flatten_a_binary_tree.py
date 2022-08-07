# Definition for a binary tree node.
from typing import Optional

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if root is None:
                return None
            # Parse right and then left
            dfs(root.right)
            dfs(root.left)
            root.right = self.prev
            root.left = None
            self.prev = root

        # Declare a previous global variable
        self.prev = None
        dfs(root)
        return root
