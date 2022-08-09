# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/range-sum-of-bst/


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root, low, high):
            if root is None:
                return 0

            if root.val >= low and root.val <= high:
                self.s += root.val
            dfs(root.left, low, high)
            dfs(root.right, low, high)

        self.s = 0
        dfs(root, low, high)
        return self.s
