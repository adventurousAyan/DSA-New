# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/sum-root-to-leaf-numbers/


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, s):
            if root is None:
                return None
            else:
                lh = dfs(root.left, s + str(root.val))
                rh = dfs(root.right, s + str(root.val))

                if lh is None and rh is None:
                    return int(str(s) + str(root.val))
                elif rh is None:
                    return lh
                elif lh is None:
                    return rh
                else:
                    return int(lh) + int(rh)

        res = dfs(root, "")
        return res
