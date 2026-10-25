# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        if root is None:
            return None
        
        lh = self.invertTree(root.left)
        rh = self.invertTree(root.right)
        root.left = rh
        root.right = lh

        return root