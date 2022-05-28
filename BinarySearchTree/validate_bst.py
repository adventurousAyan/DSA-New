# Definition for a binary tree node.
from typing import Optional

# https://leetcode.com/problems/validate-binary-search-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root, float("-inf"), float("inf"))

    def solve(self, root, leftVal, rightVal):
        if root is None:
            return True
        else:
            if not (root.val > leftVal and root.val < rightVal):
                return False
            else:
                return self.solve(root.left, leftVal, root.val) and self.solve(
                    root.right, root.val, rightVal
                )
