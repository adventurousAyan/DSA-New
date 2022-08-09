# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/validate-binary-search-tree/


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min, max):
            if root is None:
                return True

            if root.val > min and root.val < max:
                lh = dfs(root.left, min, root.val)
                rh = dfs(root.right, root.val, max)
                return lh & rh
            else:
                return False

        return dfs(root, float("-inf"), float("inf"))
