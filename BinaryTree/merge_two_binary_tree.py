# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return None
            elif root1 is None:
                return root2
            elif root2 is None:
                return root1
            else:
                root1.left = dfs(root1.left, root2.left)
                root1.right = dfs(root1.right, root2.right)
                root1.val += root2.val
                return root1

        dfs(root1, root2)
        return root1 if root1 else root2
