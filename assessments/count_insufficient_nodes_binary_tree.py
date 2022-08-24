# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        def dfs(root, su, limit):
            if root is None:
                return True

            if su + root.val < limit and root.left is None and root.right is None:
                return True

            if su + root.val >= limit and root.left is None and root.right is None:
                return False

            lh, rh = False, False

            lh = dfs(root.left, su + root.val, limit)
            rh = dfs(root.right, su + root.val, limit)
            if lh:
                root.left = None
            if rh:
                root.right = None
            return lh and rh

        res = dfs(root, 0, limit)
        if res:
            return None
        return root
