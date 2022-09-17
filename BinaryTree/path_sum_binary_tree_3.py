# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:

    # https://leetcode.com/problems/path-sum-iii/
    # Also known as k sum paths in binary tree

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root):
            if root is None:
                return

            self.ls.append(root.val)
            dfs(root.left)
            dfs(root.right)

            su = 0
            for i in range(len(self.ls) - 1, -1, -1):
                su += self.ls[i]
                if su == targetSum:
                    self.cnt += 1
            self.ls.pop()

        self.ls = []
        self.cnt = 0
        dfs(root)
        return self.cnt
