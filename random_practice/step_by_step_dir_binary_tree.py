# Definition for a binary tree node.
from typing import Optional

# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def lca(root, startValue, destValue):
            if root is None:
                return None
            if root.val == startValue or root.val == destValue:
                return root
                
            else:
                lh = lca(root.left, startValue, destValue)
                rh = lca(root.right, startValue, destValue)

                if lh is None:
                    return rh
                if rh is None:
                    return lh
                return root

        def find_path(root, val, s):
            if root is None:
                return ""
            if root.val == val:
                return s
            else:
                lh = find_path(root.left, val, s + "L")
                rh = find_path(root.right, val, s + "R")

                if lh:
                    return lh
                if rh:
                    return rh
                return ""

        lca_root = lca(root, startValue, destValue)
        str1 = find_path(lca_root, startValue, "")
        str1 = "".join(["U"] * len(str1))
        str2 = find_path(lca_root, destValue, "")
        return str1 + str2
