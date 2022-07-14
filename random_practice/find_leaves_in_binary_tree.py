# Definition for a binary tree node.
from typing import List, Optional

# https://leetcode.com/problems/find-leaves-of-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        d1 = {}

        def dfs(root, layer):
            if root is None:
                return layer
            lh = dfs(root.left, layer)
            rh = dfs(root.right, layer)

            layer = max(lh, rh)

            if layer not in d1:
                d1[layer] = [root.val]
            else:
                d1[layer] += [root.val]
            layer += 1
            return layer

        dfs(root, 0)
        return d1.values()
