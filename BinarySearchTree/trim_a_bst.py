# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/trim-a-binary-search-tree/


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        def dfs(root, low, high):
            if root is None:
                return root

            # Case 1 :- root lies outside the lower range. So root and root.left can be discarded
            if root.val < low:
                root.left = None
                root = dfs(root.right, low, high)
            # Case 2 :- root lies outside the upper range. So root and root.right can be discarded
            elif root.val > high:
                root.right = None
                root = dfs(root.left, low, high)
            else:
                root.left = dfs(root.left, low, high)
                root.right = dfs(root.right, low, high)
            return root

        return dfs(root, low, high)
