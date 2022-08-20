# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root):
            if root is None:
                return None

            dfs(root.left)
            self.ls.append(root.val)
            dfs(root.right)

        self.ls = []
        dfs(root)

        lp, rp = 0, len(self.ls) - 1

        while lp < rp:
            ss = self.ls[lp] + self.ls[rp]
            if ss < k:
                lp += 1
            elif ss > k:
                rp -= 1
            else:
                return True
        return False
