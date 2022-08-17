# Definition for a binary tree node.

# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxval):
            if root is None:
                return 0
            if root.val < maxval:
                return dfs(root.left, maxval) + dfs(root.right, maxval)

            else:
                return (
                    1
                    + dfs(root.left, max(maxval, root.val))
                    + dfs(root.right, max(maxval, root.val))
                )

        return dfs(root, float("-inf"))
